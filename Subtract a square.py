import math
import random


"""
# File Name: CS112_A1_T2_3_20230735.py
# Purpose: This is a two-player mathematical game of strategy. It is played by two
# people with a pile of coins (or other tokens) between them. The players take turns removing
# coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).
# The player who removes the last coin wins.
# Author: Mohamed Elmugtaba Omer Ahmed Hassan
# ID : 20230735
"""
print("\t\t^^^Subtract a square^^^")  # print the game title
#  print the rules of the game
print("   Rules: \n1) You will choose the number you want to start with or a random number\n2)"
      " Choose a number and it must be a perfect square"
      "\n3) Every time you choose a number, it will decrease from the first number you started with\n4)"
      " The player who reaches 0 wins\n")

# a function to check if the number is a square number or not
def check_square_number(first_player):
    if (math.ceil(math.sqrt(first_player)) ==  # check if the ceil ot sqrt of the number is equal to the floor
                                               # then the number is a perfect
            math.floor(math.sqrt(first_player))):
        return True
    else:
        return False


print("\t\t^^^The game started^^^ ")
play_again = True
the_start_number = 0
# loop to ask the players if they want to play again or not
while play_again:
    #  ask the players they want to play
    select_choose = input("\t\thow do want to start?\nA for random number: \nB to choose the number: ").upper()
    if select_choose == 'A':
        while True:
            the_start_number = random.randint(10, 1000)  # pick a random number between 10 and 1000
            the_start_number = int(the_start_number)
            if check_square_number(the_start_number):
                continue
            else:
                print(the_start_number)
                break
    elif select_choose == 'B':
        while True:  # loop to check the input
            the_start_number = input("select the number to start with: ")  # ask to set the number to start with
            if not the_start_number.isdigit():  # validate the number
                print("invalid choose!!")
                continue
            else:
                the_start_number = int(the_start_number)
                break  # exit the loop
    else:
        print("invalid choose!!")
        continue

    while True:  # loop for player 1
        first_player = input("player 1: ")  # take the input from the user
        if not first_player.isdigit():  # validate the number entered by the player
            print("invalid choose!!")
            continue
        else:
            first_player = int(first_player)
        if first_player > the_start_number:  # check if the input is bigger than the main number
            print("the number is big enter a working number ")
            continue
        elif not check_square_number(first_player):  # check if the input is not squared
            print("enter a square number! ")
            continue
        elif first_player <= 0:  # check if the input is zero or negative
            print("zero is not a choice!")
            continue
        while check_square_number(first_player):  # a while to check if the input is squared
            the_start_number -= first_player  # subtract the user number from the main number
            print(the_start_number)
            break
        if the_start_number == 0:  # check if  the last total was zero
            print("player 1 wins\n ")
            break  # end game
        while True:  # loop for player 2
            second_player = input("player 2: ")
            if not second_player.isdigit():  # validate the number entered by the player
                print("invalid choose!!")
                continue
            else:
                second_player = int(second_player)
            if second_player > the_start_number:  # check if the input is bigger than the main number
                print("the number is big enter a working number ")
                continue
            elif second_player <= 0:  # check if the input is zero or negative
                print("zero is not a choice!")
                continue
            elif not check_square_number(second_player):  # check if the input is not squared
                print("enter a square number! ")
                continue
            if check_square_number(second_player):  # check if the input is squared
                the_start_number -= second_player  # subtract the user number from the main number
                print(the_start_number)
                break
        if the_start_number == 0:  # check if  the last number was zero
            print("player 2 wins\n ")
            break  # end game
    while play_again:
        again = input("do you want to play again?\nY)yes \nN)no\n ").upper()  # ask the players to play again or not
        if again == 'Y':
            the_start_number = 0
            check_number = True
            break
        elif again == 'N':
            print("thank you for playing ")
            play_again = False
            break
        else:
            print("Enter a Valid Input ")
