'''

NAME:   Ke'niah Williams

DATE:   September 30th, 2022

ASSN:   LAB ASSIGNMENT L3

DESC:   THE FOLLOWING PYTHON MODULE IMPLEMENTS THE FAMOUS ROCK,
        PAPER, SCISSORS GAME.  THE RULES OF THE GAME ARE SIMPLE.
        EACH PLAYER CHOOSES A ROCK (0), PAPER(1), OR SCISSORS (2).
        THE FOLLOWING ARE WINNING PLAYS:
        
        ROCK BEATS SCISSORS
        PAPER BEATS ROCK
        SCISSORS BEATS PAPER

'''

# COMPUTER CHOOSES ROCK, PAPER, OR SCISSORS BASED ON A RANDOM
# INTEGER CHOICE USING THE RANDINT() FUNCTION.
# COMPUTER IS PLAYER 1
from random import randint
computer_choice = randint(0,2)
def menu():
    print("Choose a mode")
    print("1-Single Play")
    print("2-Multiple Plays")
    print("3-Quit the game")


def single_play():
    print("Rock is 0, Paper is 1, Scissors is 2")
    user_choice = int(input("Please make a selection: "))
    print()
    if (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
        print("Player 1 Wins! they chose: " + str(computer_choice))
    elif computer_choice == user_choice:
        print("Its a tie")
    else:
        print("Player 2 Wins! they chose: " + str(user_choice))
    print()
     
def multiple_plays(plays):
    for multiple in range(plays):
        computer_choice = randint(0,2)
        print("Rock is 0, Paper is 1, Scissors is 2")
        user_choice = int(input("Please make a selection: "))
        print()
        if (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
            print("Player 1 Wins! they chose: " + str(computer_choice))
        elif computer_choice == user_choice:
            print("Its a tie")
        else:
            print("Player 2 Wins! they chose: " + str(user_choice))
        print()
        
def quit_game():
    print("Thank you for playing!")
        
menu()
print()
mode = int(input("Please select a mode: "))

while mode != 3:
    while mode > 2:
        print("Invalid Entry")
        mode = int(input("Please select a mode: "))
     
    if mode == 1:
        print(single_play())
    elif mode == 2:
        plays = int(input("How many times would you like to play?: "))
        print(multiple_plays(plays))
    elif mode ==3:
        print(quit_game())
    else:
        print("Thank you for playing")
    menu()
    mode = int(input("Please select a mode: "))


# GET THE USER CHOICE, user_choice, USING THE input() function
# TYPECAST AS AN INTEGER
# USER IS PLAYER 2
#print("Rock is 0, Paper is 1, Scissors is 2")
#user_choice = int(input("Please make a selection: "))

 #if (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
    #print("Player 1 Wins! they chose: " + str(computer_choice))

#elif computer_choice == user_choice:
    #print("Its a tie")
#else:
    #print("Player 2 Wins! they chose: " + str(user_choice))




# IMPLEMENT THE RULES OF THE GAME USING IF-ELIF-ELSE STATEMENTS
# BE SURE TO USE COMPARISON AND BOOLEAN OPERATORS
# IF PLAYER 1 CHOOSES ROCK AND PLAYER 2 CHOOSES SCISSORS, OR
# IF PLAYER 1 CHOOSES PAPER AND PLAYER 2 CHOOSES ROCK, OR
# IF PLAYER 1 CHOOSES SCISSORS AND PLAYER 2 CHOOSES PAPER, THEN
# PLAYER 1 WINS

# ELSE IF PLAYER 1 AND PLAYER 2 CHOOSES THE SAME OBJECT, THEN
# IT'S A TIE
#
# OTHERWISE, PLAYER 2 WINS
#if (computer_choice == 0 and user_choice == 2) or (computer_choice == 2 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
    #print("Player 1 Wins! they chose: " + str(computer_choice))

#elif computer_choice == user_choice:
    #print("Its a tie")
#else:
    #print("Player 2 Wins! they chose: " + str(user_choice))


# PRINT THE WINNER AND THEIR CHOICE



###############
### THE END ###
###############


