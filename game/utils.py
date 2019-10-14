def Enter(symbol, pos, board):
    """We insert a letter into our game
    args:
        symbol: the selected element
        pos: The position we are inserting the element
    """
    if pos:
        board[pos] = symbol


def winGame(t, c):
    """function to check if we have a winner basing on all winning combinations
    args
        t: list representing symbols of X and O drawn on the game board
        c: symbol either X or O to check if there is a winner basing on combinations
    """
    return (
        (t[1] == c and t[2] == c and t[3] == c)
        or (t[4] == c and t[5] == c and t[6] == c)
        or (t[7] == c and t[8] == c and t[9] == c)
        or (t[1] == c and t[4] == c and t[7] == c)
        or (t[2] == c and t[5] == c and t[8] == c)
        or (t[3] == c and t[6] == c and t[9] == c)
        or (t[1] == c and t[5] == c and t[9] == c)
        or (t[3] == c and t[5] == c and t[7] == c)
    )


def boardFull(board):
    """function to check wether the board is full"""
    if board.count(" ") == 0:
        return True
    return False
