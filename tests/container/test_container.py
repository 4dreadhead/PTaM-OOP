import unittest
from lib.container import Container


class TestContainer(unittest.TestCase):
    def setUp(self) -> None:
        self.container = Container()

    def test_initialized(self):
        self.assertEqual(
            self.container.data,
            [],
            msg="'data' must be initialized correctly"
        )
        self.assertEqual(
            self.container.size,
            0,
            msg="'size' must be 0 after initialize"
        )
        self.assertEqual(
            self.container.max_size,
            Container.MAX_CONTAINER_SIZE,
            msg="'max_size' must be same as 'Container.MAX_CONTAINER_SIZE'"
        )

    def test_add(self):
        self.container.add(0)
        self.container.add(1)
        self.container.add(2)

        self.assertEqual(
            self.container.data,
            [0, 1, 2],
            msg="'#add' must add data to container"
        )
        self.assertEqual(
            self.container.size,
            3,
            msg="'size' must be increased by each added object"
        )

        for i in range(3, Container.MAX_CONTAINER_SIZE):
            self.container.add(i)

        self.assertRaises(
            BufferError,
            self.container.add,
            "one more element for full container"
        )

    def test_clear(self):
        self.container.clear()

        self.assertEqual(
            self.container.data,
            [],
            msg="'#clear' must clear container data"
        )
        self.assertEqual(
            self.container.size,
            0,
            msg="'#clear' must set 'size' at 0"
        )

    def test_sort(self):
        class TestAnimal:
            def __init__(self, name):
                self.name = name

        short_name_animal = "short"
        medium_length_name_animal = "not_too_short"
        long_name_animal = "very_very_very_long_name"

        for animal_name in [long_name_animal, medium_length_name_animal, short_name_animal]:
            self.container.add(TestAnimal(animal_name))

        self.container.sort_by_name_length()

        self.assertEqual(
            [animal.name for animal in self.container.data],
            [short_name_animal, medium_length_name_animal, long_name_animal],
            msg="'#sort' must sort descending container data"
        )
