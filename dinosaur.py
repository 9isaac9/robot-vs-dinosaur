class Dinosaur:

    def __init__(self):
        self.name = "Dino"
        self.attack_power_point_reducer = 20
        self.health = 100

    def attack(self, robot):
        
        robot.health -= self.attack_power_point_reducer
        print(f"{self.name} attacked {robot.name} for {self.attack_power_point_reducer} leaving {robot.name} with {robot.health} health remaining")


