def ask_int(question):

    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Please enter a valid interger.")

def ask_float(question):

    while True:
        try:
            return float(input(question))
        except ValueError:
            print("Please enter a valid number.")

def ask_yes_no(question):

    while True:

        ans = input(question + "(y/n): ").lower()

        if ans in ["y", "yes"]:
            return True
        elif ans in ["n", "no"] :
            return False
        else:
            print("Please enter y or n")

