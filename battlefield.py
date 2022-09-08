from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.robot = Robot()
      
    
    
          
    def run_game(self): #this is going to act like a controller it will call all my other fruncitons
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
     
    def display_welcome(self):
        print("\nwelcome to an epic battle for the ages!\nOnly one side can win!\n")

    def battle_phase(self):
        # self.attack_power_point_reducer = 20 (20x2=100hp) means dino lose all 100hp=0
        print("STARTING BATTLEPHASE!!!")
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

        
       
    def display_winner(self):
        if self.robot.health > 0:
            print("Robot wins!!!")    
        else:
            print("Dino Wins!!!") 
