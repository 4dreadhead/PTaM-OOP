from lib.container import Container
from lib.animals import *
import sys
from accessify import private


class Worker:
    """
    Application worker
    """
    def __init__(self):
        self.__container = Container()

    def run(self, file_in, file_out):
        self.read_data_from_file(file_in)
        self.__container.sort_by_name_length()
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
