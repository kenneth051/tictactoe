from game.board import drawBoard
from game.players import Ai, playerOneMove
from game.utils import boardFull, winGame, Enter

board = [" " for x in range(10)]
board[0]="-"

def main():
    """main function to run the game"""
    drawBoard(board)
    while not (boardFull(board)):
        if not (winGame(board, "X")):
            move = Ai(board)
            if move == 0:
                return "Game is a Tie"
            else:
                Enter("O", move, board)
                print("I have placed an O at position " + str(move) + " , your turn")
                drawBoard(board)
        else:
            return "You won, Congrats"
        if not (winGame(board, "O")):
            playerOneMove(board)
            drawBoard(board)
        else:
            return "better luck next time, I HAVE WON"
    return "Game is a tie"
