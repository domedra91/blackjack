#tictactoe intro
import random

print("----------------------------------------------------------------------------------------------------------------------------")
print("Welcome to the game of Tic-Tac-Toe!  You will be playing against the computer.")
print()
gameboard1 = [1,2,3]
gameboard2 = [4,5,6]
gameboard3 = [7,8,9]
available_spaces = [1,2,3,4,5,6,7,8,9]
available_spaces = [item for item in available_spaces if isinstance(item, int)] 
winner = False

#randomize player 1
print("Let's start with randomizing Player 1...")
player = int(random.randint(1,100))
computer = int(random.randint(1,100))

#player 1 is player
if player > computer:
    p1 = "player"
    p2 = "computer"
    print("Player 1 will be the player and mark with an X")
    print("Player 2 will be the computer and mark with an O")
    print()
    print("If you are ready, let's start the game.  Press '1' to start")
    start_game = int(input())

#player 1 is computer
else:
    p1 = "computer"
    p2 = "player"
    print("Player 1 will be the computer and mark with an X")
    print("Player 2 will be the player and mark with an O")
    print()
    print("If you are ready, let's start the game.  Press '1' to start")
    start_game = int(input())


def gameboard():
    print("Live Game")
    print(gameboard1)
    print(gameboard2)
    print(gameboard3)

#mark list of available numbers after p1
def mark_options_p1(number):
    available_spaces[number-1] = "X"
    print("")
    return available_spaces

#mark list of available numbers after p2
def mark_options_p2(number):
    available_spaces[number-1] = "O"
    print("")
    return available_spaces

#mark game grid p1
def mark_grid_p1(number):
    if 1 <= number <= 3:
        gameboard1[number-1] = "X"
    elif 4 <= number <= 6:
        gameboard2[number-4] = "X"
    else:
        gameboard3[number-7] = "X"
    return gameboard1, gameboard2, gameboard3

#mark game grid p2
def mark_grid_p2(number):
    if 1 <= number <= 3:
        gameboard1[number-1] = "O"
    elif 4 <= number <= 6:
        gameboard2[number-4] = "O"
    else:
        gameboard3[number-7] = "O"
    return gameboard1, gameboard2, gameboard3


#winning scenarios
def check_winner():
    #horizontal
    if gameboard1[0] == gameboard1[1] == gameboard1[2]:
        winner = True
        print("Winner!")
    elif gameboard2[0] == gameboard2[1] == gameboard2[2]:
        winner = True
        print("Winner!")
    elif gameboard3[0] == gameboard3[1] == gameboard3[2]:
        winner = True
        print("Winner!")

    #vertical
    elif gameboard1[0] == gameboard2[0] == gameboard3[0]:
        winner = True
        print("Winner!")
    elif gameboard1[1] == gameboard2[1] == gameboard3[1]:
        winner = True
        print("Winner!")
    elif gameboard1[2] == gameboard2[2] == gameboard3[2]:
        winner = True
        print("Winner!")

    #diagonal
    elif gameboard1[0] == gameboard2[1] == gameboard3[2]:
        winner = True
        print("Winner!")
    elif gameboard1[2] == gameboard2[1] == gameboard3[0]:
        winner = True 
        print("Winner!")
    else:
        winner = False
    return winner

#no winner yet
if start_game == 1:
    print("----------------------------------------------------------------------------------------------------------------------------")
    gameboard()
    print("----------------------------------------------------------------------------------------------------------------------------")
    while winner == False:
        print("Player 1 please make your choice: ")
        if p1 == "computer":


            #p1
            choice = random.choice(available_spaces)
            print(choice)
            mark_options_p1(choice)
            mark_grid_p1(choice)
            gameboard()
            print("----------------------------------------------------------------------------------------------------------------------------")
            check_winner()

            #p2
            print("Player 2, please make your choice: ")
            choice = int(input())
            mark_options_p2(choice)
            mark_grid_p2(choice)
            gameboard()
            print("----------------------------------------------------------------------------------------------------------------------------")
            check_winner()
   
        
        else:
            #p1
            choice = int(input())
            mark_options_p1(choice)
            mark_grid_p1(choice)
            gameboard()
            print("----------------------------------------------------------------------------------------------------------------------------")
            check_winner()

            #p2
            print("Player 2, please make your choice: ")
            choice = random.choice(available_spaces)
            print(choice)
            mark_options_p2(choice)
            mark_grid_p2(choice)
            gameboard()
            print("----------------------------------------------------------------------------------------------------------------------------")
            check_winner()


    #winner determined, with winning statement       
    if winner == True:
        print("We have a winner!")
        
 

else:
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("Have a nice day!") 