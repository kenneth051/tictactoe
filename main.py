from board import drawBoard
from players import Ai, playerOneMove
from utils import boardFull, winGame, Enter

board = [" " for x in range(10)]


def main():
    """main function to run the game"""
    print("welcome to tic-tac-toe\n Your symbol is 'X'")
    drawBoard(board)
    while not (boardFull(board)):
        if not (winGame(board, "O")):
            playerOneMove(board)
            drawBoard(board)
        else:
            print("better luck next time, I have won")
            break
        if not (winGame(board, "X")):
            move = Ai(board)
            if move == 0:
                print("Tie game")
                break
            else:
                Enter("O", move, board)
                print("I have placed an O at position " + str(move) + " , your turn")
                drawBoard(board)
        else:
            print("You won, Congrats")
            break


main()
