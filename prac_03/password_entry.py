"""Mitchell Marks"""

def get_password():
    password = input("Please enter a valid password: ")
    print_astriks(password)

def print_astriks(password):
    print("*" * len(password))

get_password()