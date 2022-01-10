from Characters import Character

class Goblin_War_Cheif(Character):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.power = 20
        
    def attack(self, victim):
        super().attack(victim)
        print("You do %d damage to the hero." % self.power)

    def is_alive(self):
        return super().is_alive()

    def status(self):
        super().Character_status()
        #print("The hero has %d health and %d power." % (self.health, self.power))