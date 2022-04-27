import unittest
from lib.animals import Fish


class TestFish(unittest.TestCase):
    def setUp(self) -> None:
        # Fix this line if add some new fields
        self.common_fields = {"name": "test_name", "age": "1"}

        self.fish = Fish(**self.common_fields, area=["sea", "river"])

    def test_initialized(self):
        self.assertIsInstance(
            self.fish,
            Fish,
            msg="Fish must be initialized"
        )
        self.assertEqual(
            self.fish.name,
            "test_name",
            msg="Fish must be initialized and name must be defined"
        )
        self.assertEqual(
            self.fish.age,
            1,
            msg="Fish must be initialized and age must be defined"
        )
        self.assertEqual(
            self.fish.area,
            ["sea", "river"],
            msg="Fish must be initialized and area must be defined"
        )

    def test_str(self):
        self.assertEqual(
            str(self.fish),
            f"Type: fish\t|\tName: test_name\t|\tAge: 1\t|\tArea: sea, river",
            msg="str method must return string with fish description"
        )

    def test_create_class_with_description(self):
        description = {
            "common_fields": self.common_fields,
            "unique_features": "sea+river"
        }
        wrong_description = {
            "common_fields": self.common_fields,
            "unique_features": "wrong+value"
        }
        self.assertIsInstance(
            Fish.create_class_with_description(description),
            Fish,
            msg="Method 'create_class_with_description' must return initialized Fish class"
        )
        self.assertEqual(
            Fish.create_class_with_description(description).area,
            self.fish.area,
            msg="area must be defined correctly"
        )
        self.assertRaises(
            ValueError,
            Fish.create_class_with_description,
            wrong_description
        )
