class BaseAnimal:
    """
    This is the base animal class
    """
    def __init__(self, name: str):
        """
        Initialization
        :param name: name of animal
        """
        self.name: str = name

    def __str__(self) -> str:
        """
        To string conversion, raises error when this method not defined in child class
        """
        raise NameError("__str__ method must be defined.")

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description,
        Raises error when his method not defined in child class
        :param description: animal description
        """
        raise NameError("create_class_with_description method must be defined")
