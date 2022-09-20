import random
from ai import Ai
from human import Human

class Player:
    def __init__(self):
        self.player_choice 
        self.player_score
        self.ai_choice
        self.ai_score
    
player_score = 0
ai_score = 0
print("Rock","Paper","Scissors","Lizard","Spock")
while player_score < 3 and ai_score < 3:
    player_choice = input("\nChoose 'Rock','Paper','Scissors','Lizard','Spock' \n").upper()

    while player_choice not in ["Rock","Paper","Scissors","Lizard","Spock"]:
        player_choice = input("\nChoose 'Rock','Paper','Scissors','Lizard','Spock' \n")       
    ai_choice = random.choice(['Rock','Paper','Scissors','Lizard','Spock'])
    print("Player Choice:", player_choice)
    print("AI Choice:", ai_choice)

    if player_choice == "Rock" and ai_choice == "Paper":
        ai_score += 1
    elif player_choice == "Rock" and ai_choice== "Scissors":
        player_score += 1
    elif player_choice == "Rock" and ai_choice == "Lizard":
        ai_score += 1
    elif player_choice == "Rock" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Paper" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Paper" and ai_choice == "Scissors":
        player_score += 1
    elif player_choice == "Paper" and ai_choice == "Lizard":
        ai_score += 1
    elif player_choice == "Paper" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Sissors" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Scissors" and ai_choice == "Paper":
        player_score += 1
    elif player_choice == "Scissors" and ai_choice == "Lizard":
        ai_score += 1
    elif player_choice == "Scissor" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Lizard" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Lizard"  and ai_choice == "Paper":
        player_score += 1
    elif player_choice == "Lizard" and ai_choice == "Scissors":
        ai_score += 1
    elif player_choice == "Lizard" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Spock" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Spock" and ai_choice == "Paper":
        player_score += 1
    elif player_choice == "Spock" and ai_choice == "Scissors":
        ai_score += 1
    elif player_choice == "Spock" and ai_choice == "Lizard":
        player_score += 1
    else:
        print("Tie")
    print("Player_Score:",player_score)
    print("AI Score:",ai_score)

if player_score > ai_score:
    print("\nYou win!")
else:
    print("\nYou lose")