from .base_animal import BaseAnimal


class Fish(BaseAnimal):
    """
    Class of the fish
    """
    ALLOWED_AREAS = ["canal", "lake", "ocean", "pool", "pond", "river", "sea", "spring"]

    def __init__(self, **kwargs):
        """
        Initialization
        """
        area = kwargs.pop("area")

        super().__init__(**kwargs)
        self.area = area

    def unique_features(self) -> str:
        """
        To string conversion of fish area
        :return: readable string with fish info
        """
        return f"Area: {', '.join(self.area)}"

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description
        :param description: animal description
        :return: class instance
        """
        # Unpacking BaseAnimal fields
        fish_fields = {**description["common_fields"]}

        # Parse unique fish fields
        successful_parsed_areas = []
        areas = description["unique_features"].split("+")
        for area in areas:
            if area in Fish.ALLOWED_AREAS:
                successful_parsed_areas.append(area)
        if len(successful_parsed_areas) == 0:
            raise ValueError("Unknown fish areas given")

        # Add unique fish fields
        fish_fields["area"] = successful_parsed_areas

        # Create Fish class with unpacked kwargs
        return Fish(**fish_fields)
