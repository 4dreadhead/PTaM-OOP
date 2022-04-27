from lib.container import Container
from lib.animals import *
from lib.animals.base_animal import BaseAnimal
import sys
from accessify import private
from multimethod import multimethod


class Worker:
    """
    Application worker
    """
    def __init__(self):
        self.__container = Container()

    def run(self, file_in, file_out):
        self.read_data_from_file(file_in)
        self.__container.sort_by_name_length()
        self.check_communications()
        self.write_data_to_file(file_out)
        self.__container.clear()

    @staticmethod
    def helping_info():
        """
        This function prints info for user
        :return: None
        """
        print("----------------------------------------------------------------------------------------------------")
        print("Example of command line:")
        print("app.py file_in.txt file_out.txt\n")
        print("You need to fill input file with tmp of animals.")
        print("Example in 'tmp/file_in.txt'\n")
        print(f"Default max size of container: 128.\n")
        print("----------------------------------------------------------------------------------------------------")

    @private
    def read_data_from_file(self, file_in: str):
        """
        This function reads input file and puts tmp to container
        :param file_in: path to the file
        :return: None
        """
        errors_log = []
        errors_count = 0
        try:
            with open(file_in) as file:
                lines = file.readlines()
                for index, line in enumerate(lines):
                    try:
                        self.__container.add(self.parse_line(line))
                    except (ValueError, NameError, KeyError, TypeError) as error:
                        errors_log.append(f"line {index + 1}: {str(error)}")
                        errors_count += 1
                    except BufferError:
                        print(f"! Warning: Container is full. Read only {self.__container.max_size} lines.")
                        break

            print(f"File read with {errors_count} errors.")
            if errors_log:
                print("Errors info:")
                print("\n".join(errors_log))

        except FileNotFoundError:
            print("Incorrect command line: No such input file.")
            sys.exit()

    @private
    def write_data_to_file(self, file_out: str):
        """
        This function prints container data
        :param file_out: path to output file
        :return: None
        """
        with open(file_out, "w") as file:
            print(self.__container)
            file.write(str(self.__container))

    @private
    def parse_line(self, line):
        """
        This function parses string to right animal class
        :param line: description of animal
        :return: animal
        """
        line = line.replace("\n", "").split(" ")
        if len(line) != len(BaseAnimal.DEFAULT_FIELDS) + 2:
            raise ValueError(
                f"Wrong number of arguments (expected {len(BaseAnimal.DEFAULT_FIELDS) + 2}, got {len(line)})."
            )

        common_fields = {value: line[index + 1] for index, value in enumerate(BaseAnimal.DEFAULT_FIELDS)}

        description = {
            "class_name": line[0],
            "common_fields": common_fields,
            "unique_features": line[-1].lower()
        }
        animal_class = globals()[description["class_name"]]

        return animal_class.create_class_with_description(description)

    # Multimethods area

    def check_communications(self):
        """Runs multimethods"""
        print("-" * 75)
        print("\nANIMALS COMMUNICATIONS\n")
        print("-" * 75 + "\n")

        for first_index, animal in enumerate(self.__container.data):
            for other_animal in [other for other in self.__container.data if other != animal]:
                print(f"{first_index + 1} -> {self.__container.data.index(other_animal) + 1}: ", end="")
                self.check_another_animal(animal, other_animal)
                print()
        print("-" * 75)

    @multimethod
    def check_another_animal(self, first_animal: Fish, second_animal: Fish):
        """Fish with Fish"""
        coincided_areas = [
            coincided_area for coincided_area in first_animal.area if coincided_area in second_animal.area
        ]
        if coincided_areas:
            print(
                f"a typical day between {first_animal.name} and {second_animal.name}: "
                f"'boules boules! boules boules boules, boules boules? boules boules boules...'"
            )
        else:
            print(f"{first_animal.name} and {second_animal.name} are strangers")

    @multimethod
    def check_another_animal(self, first_animal: Fish, second_animal: Beast):
        """Fish with Beast"""
        if "predator" in second_animal.beast_type:
            if "river" in first_animal.area or "lake" in first_animal.area:
                print(f"{first_animal.name} lost friends thanks to the {second_animal.name}...")
            else:
                print(
                    f"overseas friends of {first_animal.name} tell scary stories about {second_animal.name}"
                )
        else:
            print(f"{first_animal.name} hardly knows who is the {second_animal.name}")

    @multimethod
    def check_another_animal(self, first_animal: Fish, second_animal: Bird):
        """Fish and Bird"""
        if second_animal.is_migratory:
            print(f"{first_animal.name} thinks that {second_animal.name} is the alien")
        else:
            print(f"{first_animal.name} thinks thad {second_animal.name} is the annoying neighbor")

    @multimethod
    def check_another_animal(self, first_animal: Bird, second_animal: Bird):
        """Bird with Bird"""
        if first_animal.is_migratory and second_animal.is_migratory:
            print(f"{first_animal.name} and {second_animal.name} are on the same flight!")
        elif first_animal.is_migratory and not second_animal.is_migratory:
            print(f"{first_animal.name} can have a holiday romance with {second_animal.name}")
        elif not first_animal.is_migratory and second_animal.is_migratory:
            print(f"{first_animal.name} will miss for {second_animal.name} :(")
        else:
            print(f"{first_animal.name} and {second_animal.name} good neighbors! (or not so)")

    @multimethod
    def check_another_animal(self, first_animal: Bird, second_animal: Beast):
        """Bird with Beast"""
        if "predator" in second_animal.beast_type:
            print(f"{first_animal.name} needs to be careful with {second_animal.name}, ", end="")
            if first_animal.is_migratory:
                print("but not whole year")
            else:
                print("it dangerous all year round")
        else:
            print(f"{second_animal.name} and {second_animal.name} can make friends!")

    @multimethod
    def check_another_animal(self, first_animal: Bird, second_animal: Fish):
        """Bird with Fish"""
        if first_animal.is_migratory:
            print(f"{first_animal.name} will see {second_animal.name} in next year")
        if not first_animal.is_migratory:
            print(f"{first_animal.name} thinks that {second_animal.name} is a reflection of him")

    @multimethod
    def check_another_animal(self, first_animal: Beast, second_animal: Beast):
        """Beast with Beast"""
        coincided_types = [
            coincided_type for coincided_type in first_animal.beast_type if coincided_type in second_animal.beast_type
        ]

        if coincided_types:
            print(f"{first_animal.name} has same types with {second_animal.name}: {', '.join(coincided_types)}")
        else:
            print(f"{first_animal.name} and {second_animal.name} are different")

    @multimethod
    def check_another_animal(self, first_animal: Beast, second_animal: Bird):
        """Beast with Bird"""
        if second_animal.is_migratory and "predator" in first_animal.beast_type:
            print(f"{first_animal.name} could have eaten bird {second_animal.name}, ", end="")
            print("but he doesn't have much time for that, so this bird flies away soon.")
        elif not second_animal.is_migratory and "predator" in first_animal.beast_type:
            print(f"{first_animal.name} could have eaten {second_animal.name} anytime if had gotten it")
        else:
            print(f"{first_animal.name} not interested with {second_animal.name}")

    @multimethod
    def check_another_animal(self, first_animal: Beast, second_animal: Fish):
        """Beast with Fish"""
        if "predator" in first_animal.beast_type:
            if "river" in second_animal.area or "lake" in second_animal.area:
                print(f"{first_animal.name} wouldn't mind to eat {second_animal.name}")
            else:
                print(f"{first_animal.name} has no idea how delicious {second_animal.name} is")
        else:
            print(f"{first_animal.name} not interested with {second_animal.name}")
