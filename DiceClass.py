class Dice:
    def __init__(self, sides: int = 6) -> None:
        """Initialize a dice with an integer number of sides."""
        if isinstance(sides, bool) or not isinstance(sides, int):
            raise TypeError("Number of sides must be an integer.")
        if sides < 2:
            raise ValueError("Number of sides must be at least 2.")
        self.sides = sides
