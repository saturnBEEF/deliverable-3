# rework of lecture script

from items import Weapon

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, is_alive: bool = True, weapon: Weapon = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            is_alive (bool): Indicates if the character is alive (default = True)
            weapon (Weapon): The weapon the character wields
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.is_alive = is_alive
        self.weapon = weapon

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage) # calls the take_damage method of the target character
        
        if self.weapon is not None:
            weapon_damage = self.weapon.roll_damage()
            target.take_damage(weapon_damage)

    def take_damage(self, damage: int) -> None:
        """Take damage and reduce HP"""
        self._hp -= damage
        self._hp = max(self._hp, 0) # HP cannot end up lower than 0
        
        if self._hp <= 0:
            self.is_alive = False

    def heal(self, amount: int) -> None:
        """Heal and increase HP"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max) # HP cannot exceed max HP

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


# Task 4 Character Subclass

# --- Warrior subclass (Defensive Specialist)
class Warrior(Character):
    """ Warrior subclass specializing in physical defense using armor.
    
    Attributes:
        armor (int): The amount of armor reducing incoming physical damage.
    """

    def __init__(
            self,
            name: str,
            hp_max: int = 100,
            damage: int = 10,
            armor: int = 5,
            weapon: Weapon = None,
    ) -> None:
        """ Initializes a Warrior character with an armor attribute.
        
        Args:
            name (str): The name of the character.
            hp_max (int, optional): Maximum hit points. Defaults to 100.
            damage (int, optional): Base attack damage. Defaults to 10.
            armor (int, optional): Armor value reducing incoming damage. Defaults to 5.
            weapon (Weapon, optional): Equipped weapon object. Defaults to None.
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor


    def take_damage(self, damage: int) -> None:
        """ Reduces incoming damage by armor value before applying it to HP.
        
        Args:
            damage (int): The raw incoming damage amount.
        """
        # Ensure effective damage is non-negative
        effective_damage = max(0, damage - self.armor)
        super().take_damage(effective_damage)

# --- Mage subclass (Resource-Based Attacker)
class Mage(Character):
    """ Mage subclass using mana to perform powerful magic spell attacks.
    
    Attributes:
        mana (int): Current avaiable mana points.
        mana_max (int): Maximum mana capacity.
    """

    def __init__(
            self,
            name: str,
            hp_max: int = 100,
            damage: int = 10,
            mana: int = 30,
            mana_max: int = 30,
            weapon: Weapon = None,
    ) -> None:
        """ Initializes a Mage character with a mana resources.
        
        Args:
            name (str): The name of the mage.
            hp_max (int, optional): Maximum hit points. Defaults to 100.
            damage (int, optional): Base attack damage. Defaults to 10.
            mana (int, optional): Starting mana amount. Defaults to 30.
            mana_max (int, optional): Maximum mana capacity. Defaults to 30.
            weapon (Weapon, optional): Equipped weapon object. Defaults to None.
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """ Attacks the target character.

        Uses a magic spell (double base damage, ignores weapon) if mana >= 10.
        Otherwise, falls back to standard base attack (including equipped weapon)
        and recovers 5 mana.

        Args:
            target (Character): The opponentcharacter being attacked.
        """

        if self.mana >= 10:
            # Magic attack: spends 10 mana and deals double base damage (no weapon damage)
            self.mana -= 10
            magic_damage  = self.damage * 2
            target.take_damage(magic_damage)
            print(
                f"{self.name} casts a MAGIC SPELL!"
                f" (Mana remaining: {self.mana}/{self.mana_max})"
            )
        else:
            # Base attack: performs standard attack (including weapon if equipped) and restores 5 mana
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)
            print(
                f"{self.name} performs a BASE ATTACK and restores 5 mana. (Mana:"
                f" {self.mana}/{self.mana_max})"
            )