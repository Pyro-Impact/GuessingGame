from Shift15.Restart_Function import confirm_restart
import random


def random_num_generator(random_argument, user_num):
    if random_argument > user_num:
        return "Your guess is too low of a value!"
    elif random_argument < user_num:
        return "Your guess is too high of a value!"
    else:
        return "Wow, you guessed the correct value!"


while True:
    print("You have 3 guesses.")
    random_num = random.choice(range(21))
    guesses = 0
    while True:
        try:
            usernuminput = int(input("Please enter a number (0 to 20): "))
            print(random_num_generator(random_num, usernuminput))
            if usernuminput == random_num:
                break
        except ValueError:
            print("Please enter a valid number.")
        guesses += 1
        if guesses == 3:
            print("You've ran out of guesses.")
            break
    if confirm_restart() == "yes":
        continue
    else:
        break
