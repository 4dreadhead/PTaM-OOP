from .base_animal import BaseAnimal


class Bird(BaseAnimal):
    """
    Class of the fish bird
    """
    def __init__(self, **kwargs):
        """
        Initialization
        :param name: bird name
        :param is_migratory: is migratory bird
        """
        is_migratory = kwargs.pop("is_migratory")

        super().__init__(**kwargs)
        self.is_migratory = is_migratory

    def unique_features(self) -> str:
        """
        To string conversion of migratory
        :return: readable string with bird info
        """
        return f"Is migratory: {self.is_migratory}"

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description
        :param description: animal description
        :return: class instance
        """
        bird_fields = {**description["common_fields"]}

        if description["unique_features"] == "true":
            migratory = True
        elif description["unique_features"] == "false":
            migratory = False
        else:
            raise ValueError("Unknown migratory type (must be 'true' of 'false')")

        bird_fields["is_migratory"] = migratory

        return Bird(**bird_fields)
