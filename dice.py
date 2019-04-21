import os
import random


def roll_dice(quantity=1):
    os.system("cls" if os.name == "nt" else "clear")
    x = 1
    if quantity >= 2:
        while x <= quantity:
            print("Dice Number {} rolled: ".format(
                x), random.randint(1, 6))
            x += 1
    else:
        print("Your die rolled: ", random.randint(1, 6))


while True:
    print("Welcome to the dice rolling app!\n"
          "--------------------------------\n"
          "Press 1 to roll some dice.\n"
          "Press 2 to quit.\n")

    user_choice = input()
    os.system("cls" if os.name == "nt" else "clear")

    if int(user_choice) == 1:
        number_of_dice = input("How many dice do you want to roll?\n")
        roll_dice(int(number_of_dice))
        input("\nPress any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
    elif int(user_choice) == 2:
        break
    else:
        print("Invalid option.")
        input("\nPress any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
