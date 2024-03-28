import random

while True:
    highest = input("difficulty: ")
    lowest = 0
    win = False
    used_numbers = []
    while win != True:
        check = False
        random_number = random.randint(int(lowest), int(highest))
        while check != True:
            check = True
            for number in used_numbers:
                if number == random_number:
                    random_number = random.randint(int(lowest), int(highest))
                    check = False
        higher_lower = input(f"{random_number}, higher, lower, win?")
        if higher_lower == "lower":
            highest = random_number
        elif higher_lower == "higher":
            lowest = random_number
        elif higher_lower == "win":
            print("I win, let's play again")
            win = True
        else:
            print("incorect input")
        used_numbers.append(random_number)

