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
