from .base_animal import BaseAnimal


class Beast(BaseAnimal):
    """
    Class of the beast
    """
    def __init__(self, name: str, beast_type: list):
        """
        Initialization
        :param name: beast name
        :param beast_type: beast beast_type
        """
        super().__init__(name)
        self.beast_type = beast_type

    def __str__(self):
        """
        To string conversion
        :return: readable string with beast info
        """
        return f"Type: beast.\t\t Name: {self.name}.\t \tBeast type: {', '.join(self.beast_type)}."

    @staticmethod
    def allowed_beast_types() -> list:
        """
        This function returns list of the allowed beast types
        :return: list of allowed beast_types
        """
        return ["predator", "herbivores", "omnivores", "insectivores"]

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description
        :param description: animal description
        :return: class instance
        """
        successful_parsed_beast_types = []
        beast_types = description["features"].split("+")
        for beast_type in beast_types:
            if beast_type in Beast.allowed_beast_types():
                successful_parsed_beast_types.append(beast_type)
        if len(successful_parsed_beast_types) == 0:
            raise ValueError

        return Beast(name=description["name"], beast_type=successful_parsed_beast_types)
