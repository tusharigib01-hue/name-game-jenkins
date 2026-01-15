MY_NAME = "TUSHAR"

def check_name(guess):
    if not guess:
        raise ValueError("Name cannot be empty")
    return guess.upper() == MY_NAME
