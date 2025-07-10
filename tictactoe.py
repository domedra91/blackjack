#tictactoe
import random

print("Welcome to the game of TicTacToe!  You will be playing against the computer. If you are ready, press '1' to start the game")
start_game = int(input())
available_spaces = [1,2,3,4,5,6,7,8,9]
if start_game == 1:
    print("")
    print("Let's start and randomize if you are 'X' or 'O' today!")
    print("-----------------------------------------------------------------------------------------------------------------------")
    player = random.randint(1,10000)
    computer = random.randint(1,10000)
    if player > computer:
        x = "the player"
        o = "the computer"
        print("X will be " + x)
        print("O will be " + o)
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Player select which box you would like to mark: " + str(available_spaces))
    p_decision = int(input())
    choice = p_decision - 1
    if p_decision in available_spaces:
        available_spaces.pop(choice)
        print()



        print(available_spaces)





    if computer > player:
        x = "the computer"
        o = "the player"
        print("X will be " + x)
        print("O will be " + o)
    print("-----------------------------------------------------------------------------------------------------------------------")






else:
    print("No worries, we will be here once you are ready.  Have a nice day!") 