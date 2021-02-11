from Shift15.Restart_Function import confirm_restart
import random


def random_num_generator(random_argument, user_num):
    if random_argument > user_num:
        return "Your guess is too low of a value!"
    elif random_argument < user_num:
        return "Your guess is too high of a value!"
    elif random_argument == user_num:
        return "Wow, you guessed the correct value!"


guesses = 0
list_of_guesses = 0
usernuminput = 0

while True:
    print("You have 3 guesses.")
    random_num = random.choice(range(21))

    while True:
        while True:
            try:
                usernuminput = int(input("Please enter a number (0 to 20): "))
            except ValueError:
                print("Please enter a valid number.")

            if usernuminput not in range(0, 21):
                print("Please enter a number within the range of 0 to 20...")
                break
            elif usernuminput == random_num:
                break
            else:
                print(random_num_generator(random_num, usernuminput))
                break

        guesses += 1
        for i in range(1, guesses + 1):
            list_of_guesses = i

        if list_of_guesses == 3:
            print("You've ran out of guesses.")
            break
        else:
            continue

    if confirm_restart() == "yes":
        continue
    else:
        break
