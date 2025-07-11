#tictactoe
import random

print("----------------------------------------------------------------------------------------------------------------------------")
print("Welcome to the game of Tic-Tac-Toe!  You will be playing against the computer. If you are ready, press '1' to start the game")
start_game = int(input())
gameboard1 = [1,2,3]
gameboard2 = [4,5,6]
gameboard3 = [7,8,9]
available_spaces = [1,2,3,4,5,6,7,8,9]

def initial_player():
    print("Let's start with randomizing Player 1...")
    player = int(random.randint(1,100))
    computer = int(random.randint(1,100))
    if player > computer:
        p1 = player
        p2 = computer
        print("Player 1 will be the player and mark with an X")
        print("Player 2 will be the computer and mark with an O")
    else:
        p1 = computer
        p2 = player
        print("Player 1 will be the computer and mark with an X")
        print("Player 2 will be the player and mark with an O")

def initial_gameboard():
    print("The board setup")
    print(gameboard1)
    print(gameboard2)
    print(gameboard3)

def mark_choice_p1(number):
    available_spaces.pop(p_decision-1)
    print(available_spaces)

def mark_choice_p2(number):
    available_spaces.pop(p_decision-1)
    print(available_spaces)

def find_space_x(number):
    


def find_space_o(number):



if start_game == 1:
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------")
    initial_player()
    print("----------------------------------------------------------------------------------------------------------------------------")
    initial_gameboard()
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("")

else:
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("No worries, we will be here once you are ready.  Have a nice day!") 