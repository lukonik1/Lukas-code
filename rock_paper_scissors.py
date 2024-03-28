import random as rm

def prohra():
    print(f"you lose {choice} beats {player_choise}")

def vyhra():
    print(f"you win {player_choise} beats {choice}")

player = False
while player == False:
    choice = rm.choice(["rock", 'paper', 'scissors'])
    inp = input("rock, paper, scissors?: ")
    player_choise = inp.lower()
    if player_choise == choice:
        print("It's a draw")
    elif player_choise == "rock":
        if choice == "paper":
            prohra()
        else:
            vyhra()
    elif player_choise == "paper":
        if choice == "scissors":
            prohra()
        else:
            vyhra()
    elif player_choise == "scissors":
        if choice == "rock":
            prohra()
        else:
            vyhra()
    elif player_choise == "exit":
        player = True
    else:
        print ("wrong input")