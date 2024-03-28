import random


def loser(guesses, g):
    if g >= guesses:
        return "You lose"
    else:
        return f'You sill have {guesses - g} guesses'


while True:
    difficulty = int((input("The highest number: ")))
    guessing_number = random.randint(0, difficulty)
    guesses = int(input('How many guesses do you want: '))
    g = 0

    s = True
    while s == True:
        number = int(input("guess: "))
        if number == guessing_number:
            print("you won")
            s = False
        elif number > guessing_number:
            print("lower")
            g += 1
            print(loser(guesses, g))
            if loser(guesses, g) == 'You lose':
                s = False
        elif number < guessing_number:
            print("higher")
            g += 1
            print(loser(guesses, g))
            if loser(guesses, g) == 'You lose':
                s = False
