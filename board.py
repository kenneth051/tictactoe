def drawBoard(pos):
    """function for drawing the playing board
    args: 
        pos: index position to put our symbol

    """
    print(" "+str(pos[1]) +" | " +str(pos[2])+ " | "+str(pos[3]))
    print("---|---|---")
    print(" "+str(pos[4]) +" | " +str(pos[5])+ " | "+str(pos[6]))
    print("---|---|---")
    print(" "+str(pos[7]) +" | " +str(pos[8])+ " | "+str(pos[9]))

