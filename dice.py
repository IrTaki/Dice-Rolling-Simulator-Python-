import os
import random


# Dice rolling function to keep main code cleaner.
# Quantity always equals 1 in case the user doesn't enter any number.
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


while True:  # Infinite loop to keep rolling dice until the user quits.
    print("Welcome to the dice rolling app!\n"
          "--------------------------------\n"
          "Press 1 to roll some dice.\n"
          "Press 2 to quit.\n")
    user_choice = input()  # Get users choice for the menu options.
    os.system("cls" if os.name == "nt" else "clear")

    if user_choice == "1":  # Roll some dice.
        number_of_dice = input("How many dice do you want to roll?\n")
        roll_dice(int(number_of_dice))
        input("\nPress any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
    elif user_choice == "2":  # Quits the application.
        break
    else:  # Repeats the question if they enter an invalid response.
        print("Invalid option.")
        input("\nPress any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
