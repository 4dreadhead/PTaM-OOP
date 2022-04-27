import unittest
from lib.animals import Bird


class TestBird(unittest.TestCase):
    def setUp(self) -> None:
        # Fix this line if add some new fields
        self.common_fields = {"name": "test_name", "age": "1"}

        self.bird = Bird(**self.common_fields, is_migratory=True)

    def test_initialized(self):
        self.assertIsInstance(
            self.bird,
            Bird,
            msg="Bird must be initialized"
        )
        self.assertEqual(
            self.bird.name,
            "test_name",
            msg="Bird must be initialized and name must be defined"
        )
        self.assertEqual(
            self.bird.age,
            1,
            msg="Bird must be initialized and age must be defined"
        )
        self.assertEqual(
            self.bird.is_migratory,
            True,
            msg="Bird must be initialized and is_migratory must be defined"
        )

    def test_str(self):
        self.assertEqual(
            str(self.bird),
            f"Type: bird\t|\tName: test_name\t|\tAge: 1\t|\tIs migratory: True",
            msg="str method must return string with bird description"
        )

    def test_create_class_with_description(self):
        description = {
            "common_fields": self.common_fields,
            "unique_features": "true"
        }
        wrong_description = {
            "common_fields": self.common_fields,
            "unique_features": "wrong+value"
        }
        self.assertIsInstance(
            Bird.create_class_with_description(description),
            Bird,
            msg="Method 'create_class_with_description' must return initialized Bird class"
        )
        self.assertEqual(
            Bird.create_class_with_description(description).is_migratory,
            self.bird.is_migratory,
            msg="is_migratory must be defined correctly"
        )
        self.assertRaises(
            ValueError,
            Bird.create_class_with_description,
            wrong_description
        )
