# Hiding implementation details
#eg. reigstration process where we separate concern(user input, vaildating, saving)

def get_input():
    print("getting user input")

def validate_input():
    print('validating user info')

def save_to_db():
    print('saving to database')

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("Succesfully Registered!")

register_user()