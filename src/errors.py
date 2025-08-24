class InvalidDiceError(Exception):
    """Exception raised for invailed dice value."""
    def __init__(
            self,
            message="Invalid dice value. Value must be greater than 1."
    ):
        self.message = message
        super().__init__(self.message)

class DiceAlreadyExistsError(Exception):
    """Exception raised for duplicate dice value."""
    def __init__(
            self,
            message="Dice already exists."
    ):
        self.message = message
        super().__init__(self.message)

class DiceNotFoundError(Exception):
    """Exception raised for dice not found."""
    def __init__(
            self,
            message="Dice not found."
    ):
        self.message = message
        super().__init__(self.message)