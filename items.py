from DiceClass import Dice

class Weapon:
    """ Representing a weapon in the game """

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        initialise the weapon
        
        args:
            name (str): name of the weapon
            damage_dice (Dice): The dice used to calculate damage
        """

        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """ Roll the damage dice to calculate damage """
        return self.damage_dice.roll()