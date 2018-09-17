import random

class Ability:
    def __init__(self, name, attack_strength): # Initalize starting values
        # Set Ability name
        self.name = name
        # Set attack strength
        self.attack_strength = attack_strength

    def attack(self): # Return attack value
        # Calculate lowest attack value as an integer
        lowest_attack_value = self.attack_strength // 2
        # Use random.randit(a, b) to select a random attack value.
        attack_strength = random.randint(lowest_attack_value, self.attack_strength)
        # Return attack value between 0 and the full attack
        return attack_strength

    def update_attack(self, attack_strength): # Update attack value
        attack_value = attack_strength

class Hero:
    def __init__(self, name):
        # Initialize starting values
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        total_attack = 0
        for add_attack in self.abilities:
            total_attack += add_attack.attack()
        return total_attack

if __name__ == "__main__": # If you run this file from the terminal this block is executed.
    print("Hello World")
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
