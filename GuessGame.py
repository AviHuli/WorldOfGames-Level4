def generate_number(difficulty):
    import random
    secret_number = random.randint(1,int(difficulty))
    return secret_number

def get_guess_from_user(difficulty,secret_number):
    user_guess = int(input("\n\n\n\n\nPlease guess a number between 1 to " + difficulty + " : "))
    return user_guess


def compare_results(user_guess, secret_number):
    if secret_number == user_guess:
        return True
    else:
        return False

def play(difficulty,name):
    secret_number = int(generate_number(difficulty))
    user_guess = int(get_guess_from_user(difficulty, secret_number))
    results = bool(compare_results(user_guess, secret_number))
    if results == True:
        print("\n\n\n", name, "You have Won !!!!!!!")
    else:
        print("\n\n\n", name, "You have Lost !!!!!!!")