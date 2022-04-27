from .base_animal import BaseAnimal


class Beast(BaseAnimal):
    """
    Class of the beast
    """
    ALLOWED_BEAST_TYPES = ["predator", "herbivores", "omnivores", "insectivores"]

    def __init__(self, **kwargs):
        """
        Initialization
        :param name: beast name
        :param beast_type: beast beast_type
        """
        beast_type = kwargs.pop("beast_type")

        super().__init__(**kwargs)
        self.beast_type = beast_type

    def unique_features(self) -> str:
        """
        To string conversion of beast type
        :return: readable string with beast info
        """
        return f"Beast type: {', '.join(self.beast_type)}"

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description
        :param description: animal description
        :return: class instance
        """
        # Unpacking BaseAnimal fields
        beast_fields = {**description["common_fields"]}

        # Parse unique beast fields
        successful_parsed_beast_types = []
        beast_types = description["unique_features"].split("+")

        for beast_type in beast_types:
            if beast_type in Beast.ALLOWED_BEAST_TYPES:
                successful_parsed_beast_types.append(beast_type)
        if len(successful_parsed_beast_types) == 0:
            raise ValueError("Unknown beast types given")

        # Add unique beast fields
        beast_fields["beast_type"] = successful_parsed_beast_types

        # Create Beast class with unpacked kwargs
        return Beast(**beast_fields)
