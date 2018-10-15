from random import randint



'''
HERO CLASS
*****************************************************************
'''
class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        defense = 0
        if(self.health>0):
            for item in self.armors:
                defense += item.defend()
        return defense
        """
        This method should run the defend method on each piece of armor and calculate the total defense.
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """

    def take_damage(self, damage_amt):
        self.health-=damage_amt
        if(self.health<=0):
            self.deaths+=1
            return 1
        return 0
        """
        This method should subtract the damage amount from the
        hero's health.
        If the hero dies update number of deaths.
        """

    def add_kill(self, num_kills):
        self.kills+=num_kills
        """
        This method should add the number of kills to self.kills
        """

    def add_ability(self, ability):
        self.abilities.append(ability)
        #add ablility to ablility list

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        attack_total = 0
        for x in self.abilities:
            attack_total+=x.attack()
        return attack_total
        #run attack() on every ability hero has

    def display(self):
        print("HERO: "+self.name)
        print("Health: "+str(self.health))
        if(self.deaths>0):
            print("Kill/Death: "+str(self.kills/self.deaths))
        print("____________")
        # print("K/D ratio: "+str(self.kills/self.deaths))



'''
ABILITY CLASS
*****************************************************************
'''


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return randint(self.attack_strength // 2, self.attack_strength)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength
        #update attack val


'''
TEAM CLASS
*****************************************************************
'''


class Team:
    def __init__(self, team_name):
        """Init resourses."""
        self.name = team_name
        self.heroes = list()
        self.team_kills = 0
        self.total_health = 0

    def add_hero(self, Hero):
        self.heroes.append(Hero)
        self.total_health += self.heroes[-1].health

    def remove_hero(self, name):
        hero_removed = False
        for i in range(len(self.heroes)):
            if self.heroes[i].name==name:
                self.heroes.pop(i)
                hero_removed=True
        if(not hero_removed):
            return 0
    def find_hero(self, name):
        for i in range(len(self.heroes)):
            if self.heroes[i].name==name:
                return self.heroes[i]
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            hero.display();
        print("____________________________________")

    def attack(self, other_team):
        attack_total = 0
        for hero in self.heroes:
            print(hero.name)
            attack_total+=hero.attack()
        kills = other_team.defend(attack_total)
        self.team_kills+=kills
        for hero in self.heroes:
            hero.add_kill(kills)

        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """

    def defend(self, damage_amt):
        defense = 0
        for hero in self.heroes:
            defense+=hero.defend()
        if(damage_amt > defense):
            self.total_health-=(damage_amt-defense)
            return self.deal_damage(damage_amt-defense)
        return 0
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        Return number of heroes killed in attack.
        """

    def deal_damage(self, damage):
        deaths = 0
        for hero in self.heroes:
            deaths+= hero.take_damage(damage/len(self.heroes))
        return deaths
        """
        Divide the total damage amongst all heroes.
        Return the number of heroes that died in attack.
        """

    def revive_heroes(self, health=100):
        self.total_health = 0
        for hero in self.heroes:
            hero.health = hero.start_health
            self.total_health+=hero.health
        """
        This method should reset all heroes health to their
        original starting value.
        """

    def stats(self):
        print(self.name)
        for hero in self.heroes:
            hero.display()
        print("____________________________________")
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.
        This data must be output to the terminal.
        """

    def update_kills(self):
        return self.team_kills

        """
        This method should update each hero when there is a team kill.
        """


'''
ARMOR CLASS
*****************************************************************
'''

class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        return randint(0,self.defense)
        """
        Return a random value between 0 and the
        initialized defend strength.
        """


'''
WEAPON CLASS
*****************************************************************
'''

class Weapon(Ability):
    def attack(self):
        return randint(0, self.attack_strength)

'''
ARENA CLASS
*****************************************************************
'''
class Arena:
    def __init__(self,team_size):
        self.team_size = team_size
        self.team_one = None
        self.team_two = None



    def build_team_one(self):
        self.team_one =  Team(unbreakable_input("what do you want your team to be named: "))
        print("time to create heroes, each team has "+str(self.team_size)+" heroes")
        for i in range(self.team_size):
            print("hero number {}. ".format(i))
            self.team_one.add_hero(create_hero())

        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        self.team_two =  Team(unbreakable_input("what do you want your team to be named: "))
        print("time to create heroes, each team has "+str(self.team_size)+" heroes")
        for i in range(self.team_size):
            print("hero number {}. ".format(i))
            self.team_two.add_hero(create_hero())
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        print("hi")
        while(self.team_one.total_health>0 and self.team_two.total_health>0):
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            self.show_stats()
        if(self.team_one.heroes[0].deaths==1):
            return self.team_one.name
        return self.team_two.name
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """



'''
Run Code
*****************************************************************
'''

def unbreakable_input(in_string,type="string"):
    broken = True
    while broken:
        while True:
            try:
                ui = input(in_string)
                break
            except EOFError:
                print("plz be nice")
        if(type=='int'):
            try:
                return int(ui)
            except ValueError:
                print("NAN")
        else:
            if(len(ui)>0 and len(ui)<30):
                return ui


def create_hero():
    hero =  Hero(unbreakable_input("What is your heroes name: "))
    print("what abilities does your hero have: ")
    ui = None
    while(ui!="stop"):
        hero.add_ability(create_ability())
        ui = unbreakable_input("keep going: ")

    print("what weapons does your hero have: ")
    ui = None
    while(ui!="stop"):
        hero.add_ability(create_weapon())
        ui = unbreakable_input("keep going: ")

    print("what armor does your hero have: ")
    ui = None
    while(ui!="stop"):
        hero.add_armor(create_armor())
        ui = unbreakable_input("keep going: ")
    print("Hero complete")
    return hero


def create_ability():
    ability =  Ability(unbreakable_input("What is the abilities name: "),unbreakable_input("How Strong is it: ","int"))
    return ability

def create_weapon():
    weapon =  Weapon(unbreakable_input("What is the weapons name: "),unbreakable_input("How Strong is it: ","int"))
    return weapon

def create_armor():
    armor =  Armor(unbreakable_input("What is the armors name: "),unbreakable_input("How Strong is it: ","int"))
    return armor




if __name__=="__main__":
    battle_zone =  Arena(unbreakable_input("how large is your team: ","int"))
    running = True
    battle_zone.build_team_one()
    battle_zone.build_team_two()
    while(running):
        print(battle_zone.team_battle())
        ui = unbreakable_input("do you want to play again(yes/no): ")
        if(ui == "no"):
            running = False
        else:
            battle_zone.team_one.revive_heroes()
            print(battle_zone.team_one.heroes[0].health)
            battle_zone.team_two.revive_heroes()
