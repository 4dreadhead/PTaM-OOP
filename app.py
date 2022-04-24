#!venv/bin/python
from lib.worker.worker import Worker
import sys
from sys import argv


def run(args: list) -> None:
    """
    This function runs the program
    :param args: command line arguments
    :return: None
    """
    worker = Worker()

    if len(args) == 1 or args[1] == "--help" and len(args) == 2:
        worker.helping_info()
        sys.exit()

    if len(args) != 3:
        print("Incorrect command line. Waited: app.py input_file.txt output_file.txt")
        print("Add key '--help' to check more info.")
        sys.exit()

    file_in, file_out = args[1:]
    worker.run(file_in, file_out)


if __name__ == '__main__':
    console_args = argv
    run(argv)
