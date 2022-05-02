from lib.container import Container
from lib.animals import *
import sys
from accessify import private


class Worker:
    def __init__(self):
        self.__container = Container()

    def print_filtered_data(self):
        for animal_class in [Bird, Fish, Beast]:
            print(f"\nFilter by {animal_class.__name__}")
            filtered_data = self.__container.filter_by(animal_class)

            for animal in filtered_data:
                print(animal)

    def run(self, file_in, file_out):
        self.read_data_from_file(file_in)
        self.__container.sort_by_name_length()
        self.print_filtered_data()
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
        print(f"Default max size of container: 128.\n")
        print("Example of input file:")
        print("bird Stork True")
        print("bird Eagle false")
        print("bird Macaw tRuE")
        print("fish Carp river+sea+pool")
        print("fish Shark ocean\n")
        print("You can write lines in any case.\n")
        print("Last parameter for the fish: is migratory: true or false.")
        print("Last parameter for the fish: area. Write it split '+', if fish lives in different areas.")
        print('Accepted area names: "canal", "lake", "ocean", "pool", "pond", "river", "sea", "spring".\n')
        print("If you write other area, it will not be included to the list.")
        print("If optional parameter of animal will be wrong or empty, line will not be included to the container.")
        print("----------------------------------------------------------------------------------------------------")

    @private
    def read_data_from_file(self, file_in: str):
        """
        This function reads input file and puts tmp to container
        :param file_in: path to the file
        :return: None
        """
        errors_count = 0
        try:
            with open(file_in) as file:
                lines = file.readlines()
                for line in lines:
                    try:
                        self.__container.add(self.parse_line(line))
                    except (ValueError, NameError):
                        errors_count += 1
                    except BufferError:
                        print(f"! Warning: Container is full. Read only {self.__container.max_size} lines.")
                        break

            print(f"File read with {errors_count} errors.")
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
        if len(line) != 4:
            raise ValueError

        description = {
            "type": line[0].lower(),
            "name": line[1].lower(),
            "age": int(line[2]),
            "features": line[3].lower()
        }

        if description["type"] == "bird":
            animal_class = Bird
        elif description["type"] == "fish":
            animal_class = Fish
        elif description["type"] == "beast":
            animal_class = Beast
        else:
            raise ValueError

        return animal_class.create_class_with_description(description)
