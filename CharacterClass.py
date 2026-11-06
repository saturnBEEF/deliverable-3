# rework of lecture script

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, is_alive: bool = True) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            is_alive (bool): Indicates if the character is alive (default = True)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.is_alive = is_alive

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage) # calls the take_damage method of the target character

    def take_damage(self, damage: int) -> None:
        """Take damage and reduce HP"""
        self._hp -= damage
        self._hp = max(self._hp, 0) # HP cannot end up lower than 0
        if self._hp <= 0:
            self.is_alive = False

    def heal(self, amount: int) -> None:
        """Heal and increase HP"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # HP cannot exceed max HP

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage} is_alive={self.is_alive}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
