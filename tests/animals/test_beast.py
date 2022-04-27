import unittest
from lib.animals import Beast


class TestBeast(unittest.TestCase):
    def setUp(self) -> None:
        # Fix this line if add some new fields
        self.common_fields = {"name": "test_name", "age": "1"}

        self.beast = Beast(**self.common_fields, beast_type=["predator"])

    def test_initialized(self):
        self.assertIsInstance(
            self.beast,
            Beast,
            msg="Beast must be initialized"
        )
        self.assertEqual(
            self.beast.name,
            "test_name",
            msg="Beast must be initialized and name must be defined"
        )
        self.assertEqual(
            self.beast.age,
            1,
            msg="Beast must be initialized and age must be defined"
        )
        self.assertEqual(
            self.beast.beast_type,
            ["predator"],
            msg="Beast must be initialized and is_migratory must be defined"
        )

    def test_str(self):
        self.assertEqual(
            str(self.beast),
            f"Type: beast\t|\tName: test_name\t|\tAge: 1\t|\tBeast type: predator",
            msg="str method must return string with beast description"
        )

    def test_create_class_with_description(self):
        description = {
            "common_fields": self.common_fields,
            "unique_features": "predator"
        }
        wrong_description = {
            "common_fields": self.common_fields,
            "unique_features": "wrong+value"
        }
        self.assertIsInstance(
            Beast.create_class_with_description(description),
            Beast,
            msg="Method 'create_class_with_description' must return initialized Beast class"
        )
        self.assertEqual(
            self.beast.beast_type,
            Beast.create_class_with_description(description).beast_type,
            msg="beast_type must be defined correctly"
        )
        self.assertRaises(
            ValueError,
            Beast.create_class_with_description,
            wrong_description
        )
