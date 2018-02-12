# Sahiti Enjeti's submission for Girls Who Code TA position

# game is designed for the player to compete with device
from random import randint
rps = ["Rock", "Paper", "Scissors"]

# player assigned to compete against device
device = rps[randint(0,2)]

player = False

while player == False:
# player == True
    player = input("Rock, Paper, Scissors?")
    # player and device have same play 
    if player == device:
        print("Tie!")
    elif player == "Rock":
        # paper trumps rock 
        if device == "Paper":
            print("You lose!", device, "covers", player)
        else:
            print("Winner winner chicken dinner!", player, "smashes", device)
    elif player == "Paper":
        if device == "Scissors":
            print("You lose!", device, "cut", player)
        else:
            print("Winner winner chicken dinner!", player, "covers", device)
    elif player == "Scissors":
        if device == "Rock":
            print("You lose...", device, "smashes", player)
        else:
            print("Winner winner chicken dinner!", player, "cut", device)
    else:
        print("Invalid play.")
        
  
    player = False
    device = rps[randint(0,2)]
