
class Character:
    def __init__(self):
        

     def attack(self, victim):
        victim.health -= self.power

    def is_alive(self):
        if self.health > 0:
            return True

    def Samurai_status(self):
        print("The Samurai has %d health and %d power." % (self.health, self.power))

    def Soldier_status(self):
        print("The Solider has %d health and %d power." % (self.health, self.power))

    def Wizard_status(self):
        ("The Wizard has %d health and %d power." % (self.health, self.power))
    
class Samurai:
    def __init__(self):

        self.health = 15
        self.power = 7
    
class Soldier:
    def __init__(self):

        self.health = 20
        self.power = 5
    
class Wizard:
    def __init__(self):

        self.health = 10
        self.power = 9