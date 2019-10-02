from utils import boardFull, Enter, winGame


def playerOneMove(board):
    if boardFull(board):
        return False
    else:
        move = input("Enter an 'X' btn 1 and 9 at position :  ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if board[move] == " ":
                    Enter("X", move, board)
                else:
                    print("This space is already occupied")
                    playerOneMove(board)
            else:
                print("The number entered must be in the range 0f 1 - 9")
                playerOneMove(board)
        except:
            print("please enter a valid integer")
            playerOneMove(board)


def Ai(board):
    openMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    for let in ["O", "X"]:
        for i in openMoves:
            boardcopy = board.copy()
            boardcopy[i] = let
            if winGame(boardcopy, let):
                move = i
                return move
    if 5 in openMoves:
        move = 5
        return move
    else:
        import random

        if len(openMoves) != 0:
            move = random.choice(openMoves)
            return move
        return 0
