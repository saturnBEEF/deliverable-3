# Task 5 (Running battles)

from CharacterClass import Character


class Battle:
    """ Manages Turn-based combat between two Character objects.
    
    Attributes:
        hero (Character): The first combatant (hero).
        enemy (Character): The second combatant (enemy).
    """

    def __init__(self, hero: Character, enemy: Character) -> None:
        """ Initializes a battle between a hero and an enemy character.

        Args:
            hero (Character): The hero character participating in combat.
            enemy (Character): The enemy character participating in combat.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """ Plays a single round of turn-based combat.

        The hero attacks the enemy first. If the enemy survies, the enemy then
        retaliates and attacks the hero.
        """

        print(f"\n--- {self.hero.name} attacks {self.enemy.name} ---")
        self.hero.attack(self.enemy)

        # Enemy retaliates only if still alive after hero's attack
        if self.enemy.is_alive():
            print(f"--- {self.enemy.name} retaliates against {self.hero.name} ---")
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """ Simulates full combat until one of the characters is no longer alive.

        Return:
            Character: The winning character object.
        """

        print(f"\n==========================================")
        print(f" BATTLE START: {self.hero.name} VS {self.enemy.name}")
        print(f"\n==========================================")

        round_count = 1

        # Loop until either hero or enemy is defeated
        while self.hero.is_alive and self.enemy.is_alive:
            print(f"\n--- ROUND {round_count} ---")
            self.play_round()
            round_count += 1

        # Determine the victor
        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"\n==========================================")
        print(f" BATTLE END! Winner: {winner.name}")
        print(f"\n==========================================")

        return winner
    
