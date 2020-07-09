

print (" \t Hello! \n Welcome to the game tic tac toe! This is a pass and play game. \n One of you will be X and one of you will be O. \n To win, you have to get either X or O in a row!")
the_board = {"1": " ", "2": " ", "3": " ", 
             "4": " ", "5": " ", "6": " ",
             "7": " ", "8": " ", "9": " " }
# def print_the_board(board):
#     print(board["7"] + "|")

def game():

    turn = "X"
    count = 0
    while (count < 9):
        print("It's you turn " + turn + ". Where do you want to move? ")
        move = input()
        if the_board[move] == " ":
            the_board.update({move : turn})
        else:
            print ("That space is already taken. Choose a new move: ")
        
        if turn == "X" :
            turn = "O"
            count += 1 
        else:
            turn = "X"
            count += 1
        print(turn)
game()




