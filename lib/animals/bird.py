from .base_animal import BaseAnimal


class Bird(BaseAnimal):
    """
    Class of the fish bird
    """
    def __init__(self, name="Not_specified", is_migratory=None):
        """
        Initialization
        :param name: bird name
        :param is_migratory: is migratory bird
        """
        super().__init__(name=name)
        self.is_migratory = is_migratory

    def __str__(self):
        """
        To string conversion
        :return: readable string with bird info
         """
        return f"Type: bird.\t\tName: {self.name}.\t  Is migratory: {self.is_migratory}."

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description
        :param description: animal description
        :return: class instance
        """
        if description["features"] == "true":
            migratory = True
        elif description["features"] == "false":
            migratory = False
        else:
            raise ValueError

        return Bird(name=description["name"], is_migratory=migratory)
