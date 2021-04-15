"""
Mini-project #1 - "rock_Spock_paper_lizard_scissors game"
'Introduction to Interactive Programming in Python' Course
RICE University - coursera.org
by Joe Warren and Scott Rixner

Student: Fredrick Ayivor
"""
import random

def name_to_number(name):
    """
    Take string name as input (rock_Spock_paper_lizard_scissors)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Enter a name that matches any of these; rock,Spock,paper,lizard,scissor"


def number_to_name(number):
    """
    Take number as input (0_1_2_3_4) and returns corresponding string
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Enter a number that matches any of these; 0, 1, 2, 3, 4"


# Function implementation of the game RPSLS

def rpsls(player_choice):
    """
     This is what the player chooses
    """

    print("")

    # print out the message for the player's choice
    print("Player chooses", player_choice)
    # convert player_choice to player_number using name_to_number
    player_number = name_to_number(player_choice)
    #print("Player chooses", player_number)

    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(0, 5)
    #print("Computer chooses", computer_number)

    # convert comp_number to name using number_to_name
    computer_name = number_to_name (computer_number)
    print("computer chooses", computer_name)

    # print results
    #print("Player chooses", player_choice)

    # compute difference of player_number and computer_number modulo five
    difference = (player_number - computer_number) % 5
    #print("diff:",difference)

    # use if/elif/else to determine winner
    if difference == 0:
        print("Player and computer tie!")
    elif difference == 1 or difference == 2:
        print( "Player wins!")

    #elif computer_name == player_choice:
    #    print( "Player wins")


    else:
        print( "Computer wins!")




# def rpsls(player_choice):
#     """
#     This is what the player chooses
#     """
#     print("")
#     print("Player chooses")
#     name = ["rock", "Spock", "paper", "lizard", "scissors"]
#     for indx, item in enumerate(name):
#         if player_choice == item:
#             return name_to_number(item)
#         elif player_choice == indx:
#             return number_to_name(indx)
#     import random
#     computer_number = random.randrange(5)
#     print(computer_number)
#     if rpsls(player_choice) == computer_number:
#         print("Player wins")
#
#     else:
#         print("Player lost")


# print(name_to_number("rock"))
# print(name_to_number("Spock"))
# print(name_to_number("paper"))
# print(name_to_number("lizard"))
# print(name_to_number("scissors"))
# print(name_to_number("Dog"))
# print(number_to_name(0))
# print(number_to_name(1))
# print(number_to_name(2))
# print(number_to_name(3))
# print(number_to_name(4))
# print(number_to_name(10))
# test my code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
