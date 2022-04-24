from .base_animal import BaseAnimal


class Fish(BaseAnimal):
    """
    Class of the fish
    """
    def __init__(self, name: str, area: list):
        """
        Initialization
        :param name: fish name
        :param area: fish area
        """
        super().__init__(name)
        self.area = area

    def __str__(self):
        """
        To string conversion
        :return: readable string with fish info
        """
        return f"Type: fish.\t\t Name: {self.name}.\t \tArea: {', '.join(self.area)}."

    @staticmethod
    def allowed_areas() -> list:
        """
        This function returns list of the allowed areas for the fish
        :return: list of allowed areas
        """
        return ["canal", "lake", "ocean", "pool", "pond", "river", "sea", "spring"]

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description
        :param description: animal description
        :return: class instance
        """
        successful_parsed_areas = []
        areas = description["features"].split("+")
        for area in areas:
            if area in Fish.allowed_areas():
                successful_parsed_areas.append(area)
        if len(successful_parsed_areas) == 0:
            raise ValueError

        return Fish(name=description["name"], area=successful_parsed_areas)
