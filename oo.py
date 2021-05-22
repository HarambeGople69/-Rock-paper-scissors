import time
import os
import random
import sys

name = input("Enter players name: ")
os.system("cls")
time.sleep(2)
print("Hello player, " + name + "!!")

"""MAIN MENU"""


def main_menu():
    time.sleep(2)
    print("""WELCOME TO ROCK PAPER SCISSORS GAME!!!
----- MAIN MENU -----

Press 1 for Help
press 2 for Play
Press 3 for Quit

HOPE YOU WILL HAVE GOOD EXPERINECE!
    """)

    try:
        player_choice = int(input("Enter your choice: \n"))
    except ValueError:
        os.system("cls")
        print("Invalid choice. Please choose valid choice!\n")
        main_menu()

    if player_choice == 1:
        os.system("cls")
        help_desk()
        main_menu()

    elif player_choice == 2:
        os.system("cls")
        play()

    elif player_choice == 3:
        os.system("cls")
        game_quit()


"""HELP DESK"""


def help_desk():
    print("""
----- HELP MENU -----

This information will help you for the rule
Game has 3 elements and 3 conditions
Rock, Paper and Scissors

Rock crushes scissors.
Scissors cuts paper.
Paper covers Rock.

Game will ask you to input your choice and result will be printed.
To choose an element press:

R for Rock.
P for Paper.
S for Scissors.

----- GOOD LUCK -----
""")
    time.sleep(3)
    main_menu()


def game_quit():
    os.system("cls")
    sys.exit("Thank you for playing. See you next time.")


def play():
    player = input(
        "Please enter your element:\nR for Rock\nP for Paper\nS for Scissors:\n")
    if player == "R" or player == "r":
        print("You have choosed rock.")
    elif player == "P" or player == "p":
        print("You have choosed Paper.")
    elif player == "S" or player == "s":
        print("You have choosed Scissors.")
    else:
        print("Invalid choice. Please enter correct choice.")
        play()

    comp_choice = ["P", "p", "s", "S", "r", "R"]
    comp = random.choice(comp_choice)
    time.sleep(3)

    if comp == "P" or comp == "p":
        print("Computer has choosed paper.")
    elif comp == "S" or comp == "s":
        print("Computer has choosed scissors.")
    else:
        print("Computer has choosed rock.")

    if player == "r" or player == "R":

        if comp == "s" or comp == "S":
            print("Your rock crushed computer's scissors. You win!!")
            time.sleep(2)

        elif comp == "p" or comp == "P":
            print("Computer's paper covered your rock. You lose!!")
            time.sleep(2)

        else:
            print("Its a tie!!")
            time.sleep(2)

    if player == "s" or player == "s":

        if comp == "s" or comp == "S":
            print("Its a tie!!")
            time.sleep(2)

        elif comp == "p" or comp == "P":
            print("Your scissors cut computer's paper. You win!!")
            time.sleep(2)

        else:
            print("Computer rock crushed your's scissors. You lose!!")
            time.sleep(2)

    if player == "p" or player == "P":

        if comp == "P" or comp == "p":
            print("Its a tie!!")
            time.sleep(2)

        elif comp == "s" or comp == "S":
            print("Computer's scissors cut your's paper. You lose!!")
            time.sleep(2)

        else:
            print("Your's paper covered computer's rock. You win!!")
            time.sleep(2)

    play_again()


def play_again():
    try:
        choice = int(input("""
Please select
1 - New Game
2 - Quit\n"""))
    except ValueError:
        print("Invalid selection. Please enter correct selection.")
        play_again()
    if choice == 1:
        os.system("cls")
        print("New game.\n")
        play()
    elif choice == 2:
        game_quit()
    else:
        print("Invalid selection. Please enter correct selection.")
        play_again()


main_menu()
