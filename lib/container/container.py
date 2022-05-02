class Container:
    """
    This is class of the container
    """
    MAX_CONTAINER_SIZE = 128

    def __init__(self):
        """
        Initialization
        """
        self.size = 0
        self.max_size = Container.MAX_CONTAINER_SIZE
        self.data = []

    def add(self, animal) -> None:
        """
        Adds animal to container
        :param animal: animal to add
        :return: None
        """
        if self.size >= self.max_size:
            raise BufferError

        self.data.append(animal)
        self.size += 1

    def clear(self):
        """
        This function clears container
        :return: None
        """
        self.size = 0
        self.data.clear()

    def sort_by_name_length(self):
        """
        This function sorts animals by length of name in ascending order
        :return: None
        """
        if self.size == 0:
            print("Empty container.")
            return

        for index, animal in enumerate(self.data):
            print(f"{index + 1}: name: {animal.name}, length: {len(animal.name)}")

        for _ in range(self.size):
            for i in range(self.size - 1):
                if len(self.data[i].name) > len(self.data[i + 1].name):
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]

        print("Container sorted by name length.\n")

    def filter_by(self, animal_class):
        return [animal for animal in self.data if type(animal) is animal_class]

    def __str__(self) -> str:
        """
        This function prints container tmp
        :return: str: container tmp
        """
        data = f"Animal count: {self.size}."

        if self.size > 0:
            data += " Animals:\n"

            for i in range(self.size):
                data += f"{i + 1}: {self.data[i]}\n"

        return data
