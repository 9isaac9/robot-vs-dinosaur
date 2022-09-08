from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = "Robo"
        self.health = 100
        self.active_weapon = Weapon("laser beam",25)
        
    def attack(self, dinosaur):
        
        dinosaur.health -= self.active_weapon.attack_power_point_reducer
        print(f"{self.name} attacked {dinosaur.name} for {self.active_weapon.attack_power_point_reducer} leaving {dinosaur.name} with {dinosaur.health} remaining")
    