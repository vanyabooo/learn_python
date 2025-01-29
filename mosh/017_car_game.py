command = ""
started = False

while True:
    command = input("> ")
    if command.lower() == "start":
        if started:
            print(f"Damn, the car was already started ;(")
        elif not started:
            print(f"Car started... Ready to go!")
            started = True
    elif command.lower() == "stop":
        if not started:
            print(f"Damn, the car wasn't started ;(")
        elif started:
            print(f"Car stopped.")
            started = False
    elif command.lower() == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command.lower() == "quit":
        break
    else:
        print("I don't understand the command")