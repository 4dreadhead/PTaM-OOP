import unittest
from lib.worker import Worker
import os
from app import ROOT_DIR


class TestWorker(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker()

    def test_run(self):
        file_in = os.path.join(ROOT_DIR, "tests", "tmp", "test_input.txt")
        file_out = os.path.join(ROOT_DIR, "tests", "tmp", "test_output.txt")
        file_example = os.path.join(ROOT_DIR, "tests", "tmp", "output_example.txt")

        self.worker.run(file_in, file_out)

        with open(file_out, "r+") as file, open(file_example, "r+") as example:
            self.assertEqual(
                file.read(),
                example.read(),
                msg="Worker' must read input file and write right content."
            )
            file.truncate(0)
