game_status = "on"
car_start = False
while True:
    game_status = input(">").lower()
    if game_status == "start":
        if car_start == True:
            print("What are you doing, the car has already started.")
        else:
            print("Car started...Ready to go!")
            car_start = True
    elif game_status == "stop":
        if car_start != True:
            print("What are you doing, the car has already stopped.")
        else:
            print("Car stopped.")
            car_start = False
    elif game_status == "help":
        print("""
start - to start the cargit st
stop - to stop the car
quit - to exit
""")
    elif game_status == 'quit':
        break
    else:
        print("I don't understand that...")
