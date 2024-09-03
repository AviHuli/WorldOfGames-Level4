import random
from time import sleep
sequence = []
user_sequence_list = []
def generate_sequence(difficulty):
    sequence = []
    for i in range(int(difficulty)):
        sequence.append(random.randint(1,101))
    return sequence

def get_list_from_user(difficulty):
    user_sequence_list = []
    i = 0
    while i < (int(difficulty)):
        user_sequence_list.append(int(input("\nPlease enter numbers : ")))
        i += 1
    return user_sequence_list

def is_list_equal(sequence, user_sequence_list):
    if sequence == user_sequence_list:
        return True
    else:
        return False

#def play(difficulty):
def play(difficulty, name):
    sequence = generate_sequence(int(difficulty))

    print("System sequence numbers: ", sequence)
    sleep(5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    user_sequence_list = get_list_from_user(int(difficulty))

    results = bool()
    results = is_list_equal(sequence, user_sequence_list)

    if results == True:
        print("\n\n\n\nUser sequence numbers: ", user_sequence_list, "  System sequence numbers: ", sequence)
        print("\n", name, "You have Won !!!!!!!")
        return results
    else:
        print("\n\n\n\nUser sequence numbers: ", user_sequence_list, "  System sequence numbers: ", sequence)
        print("\n", name, "You have Lost !!!!!!!")
        return results