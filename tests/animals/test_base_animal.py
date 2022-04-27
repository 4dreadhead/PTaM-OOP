import unittest
from lib.animals.base_animal import BaseAnimal


class TestBaseAnimal(unittest.TestCase):
    def setUp(self) -> None:
        self.base_animal = BaseAnimal(name="test_name", age=15)

    def test_initialized(self):
        self.assertIsInstance(
            self.base_animal,
            BaseAnimal,
            msg="BaseAnimal must be initialized"
        )
        self.assertEqual(
            self.base_animal.name,
            "test_name",
            msg="BaseAnimal must be initialized and name must be defined"
        )
        self.assertEqual(
            self.base_animal.age,
            15,
            msg="BaseAnimal must be initialized and age must be defined"
        )

    def test_str(self):
        self.assertRaises(
            NameError,
            str,
            self.base_animal
        )

    def test_create_class_with_description(self):
        self.assertRaises(
            ValueError,
            self.base_animal.create_class_with_description,
            "test_description"
        )
