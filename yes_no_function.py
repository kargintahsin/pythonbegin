def yes_no(msg: str = "y or n ?", error_msg: str = "Just y or n!"):
    print(msg)
    while True:

        choice = input().lower()
        if choice == "y" or choice == "n":
            return choice
        else:
            print(error_msg)
