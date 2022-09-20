


class Game:
    def __init__(self):
        self.human = ("Human")
        self.Ai = ("Ai")    
        
    def run_game(self):
        self.greeting()
        self.rules_of_game()
        
      

    def greeting(self):
        print("Welcome to RPSLS")

    def rules_of_game(self):
        print("Each match will be best of three games.  Use the number key to enter your selection")
        

        print("Scissor cut Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitate Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("Rock crushes Scissors")

        print(input("How many players 1,2,or 3 for a surprise?  "))

        print("Choose Rock")
        print("Choose Paper")
        print("Choose Scissors")
        print("Choose Lizard")
        print("choose Spock")

p