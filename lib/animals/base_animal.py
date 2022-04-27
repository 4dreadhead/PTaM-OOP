class BaseAnimal:
    """
    This is the base animal class
    """
    # Here must be listed all animal default fields
    DEFAULT_FIELDS = [
        "name",
        "age"
    ]

    def __init__(self, **kwargs):
        """
        Initialization
        """
        name = kwargs.pop("name")
        self.name = name.lower()

        age = kwargs.pop("age")
        self.age = int(age)

        # Check for unexpected args
        if kwargs:
            unexpected_arguments = []
            for key, value in kwargs.items():
                unexpected_arguments.append(f"'{key}': '{value}'")
            raise TypeError(f"Got an unexpected arguments: {', '.join(unexpected_arguments)}")

    def __str__(self) -> str:
        """
        To string conversion
        """
        return f"Type: {self.__class__.__name__.lower()}\t|\t" \
               f"Name: {self.name}\t|\t" \
               f"Age: {self.age}\t|\t" \
               f"{self.unique_features()}"

    def unique_features(self) -> str:
        """
        To string conversion of unique fields, must be defined in child classes
        """
        if self.__class__.__name__ == "BaseAnimal":
            raise NameError("Class 'BaseAnimal' can be only inherited")
        else:
            raise NameError(f"Method 'unique_features' undefined in '{self.__class__.__name__}' class")

    @staticmethod
    def create_class_with_description(description):
        """
        Parse data and create animal class with given description,
        Raises error when his method not defined in child class
        :param description: animal description
        """
        raise ValueError("'create_class_with_description': unknown action")
