# Task 2: Introducing randomness with a Dice class
import random


class Dice:
    def __init__(self, sides: int = 6) -> None:
        """Initialize a dice with an integer number of sides."""
        if isinstance(sides, bool) or not isinstance(sides, int):
            raise TypeError("Number of sides must be an integer.")
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Return a random integer between 1 and the number of sides."""
        return random.randint(1, self.sides)