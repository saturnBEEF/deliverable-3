# Task 5 (Running battles)

from CharacterClass import Character


class Battle:
    """ Manages Turn-based combat between two Character objects.
    
    Attributes:
        hero (Character): The first combatant (hero).
        enemy (Character): The second combatant (enemy).
    """

    def __init__(self, hero: Character, enemy: Character) -> None:
        """ Initializes a Battle instance with two Character objects.

        Args:
            hero (Character): The first combatant (hero).
            enemy (Character): The second combatant (enemy).
        """
        self.hero = hero
        self.enemy = enemy
