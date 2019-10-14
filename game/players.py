from game.utils import boardFull, Enter, winGame

selected_moves={
    1:[2,4],
    3:[2,6],
    7:[8,4],
    9:[8,6]
}

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
    """ This function implements our AI"""
    openMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    for let in ["O", "X"]:
        for i in openMoves:
            boardcopy = board.copy()
            boardcopy[i] = let
            if winGame(boardcopy, let):
                move = i
                return move
    #check if there are open moves
    if len(openMoves) == 0:
        return 0
    #check if the center is open
    if 5 in openMoves:
        move = 5
        return move
    else:
        #selects a winning move combination
        for k, v in selected_moves.items():
            if k in openMoves:
                return k
            elif k not in openMoves and boardcopy[k] == "O":
                for v in openMoves:
                    return v
