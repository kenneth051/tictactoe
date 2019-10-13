import unittest
from unittest.mock import patch
from io import StringIO 
import sys
import builtins
from ..main import main
from ..board import drawBoard
from ..players import playerOneMove,Ai
from ..utils import Enter, boardFull, winGame

class TicTacToe_Test(unittest.TestCase):
    def setUp(self):
        self.a=[" " for i in range(10)]
        
    def test_board(self):
        output=StringIO()
        sys.stdout=output
        drawBoard(self.a)
        self.assertTrue(output.getvalue())
    
    def test_enter_symbol(self):
        Enter("X", 6, self.a)
        self.assertEqual(self.a[6],"X")
        
    def test_board_full_function_returns_False(self):
        self.assertEqual(boardFull(self.a),False)
        
    def test_board_full_function_returns_true(self):
        a=["O" for i in range(10)]
        self.assertEqual(boardFull(a),True)
        
    def test_wingame_function(self):
        a=["-"," ","O","X"," ","X","6","X","O","O",]
        self.assertEqual(winGame(a,"X"),True)
    
    def test_AI_player(self):
        #test Ai moves to center
        move=Ai(self.a)
        self.assertEqual(move,5)
        #test ai moves to position one
        a=["-"," ","O","X"," ","X","X","O","O","O"]
        move=Ai(a)
        self.assertEqual(move,1)
        #test ai return 0 when there is no available move
        a=["-","I","O","X","J","X","X","O","O","O"]
        move=Ai(a)
        self.assertEqual(move,0)
        #ai wins a game
        a=["-"," ","O","X"," ","X","6","","O","O",]
        move=Ai(a)
        self.assertEqual(move,1)
    
    @patch('builtins.input', return_value=3)
    def test_player_plays_with_a_full_board(self,mock_stdout):
        a=["-","I","O","O","J","X","X","O","O","O"]
        self.assertEqual(playerOneMove(a), False)
        
    @patch('builtins.input', side_effect=["u",3])
    def testdictCreateSimple(self,mock_stdout):
        a=["-","I","O"," ","J","X","X","O","O","O"]
        output=StringIO()
        sys.stdout=output
        playerOneMove(a)
        self.assertEqual(output.getvalue(), 'please enter a valid integer\n')
    
    @patch('builtins.input', side_effect=[4,4,5,])
    def test_player_one(self,mock_stdout):
        b=["-","I","O"," "," "," ","X","O","O","O"]
        self.assertEqual(b[4]," ")
        playerOneMove(b)
        print(b[4])
        self.assertEqual(b[4],"X")
    
    @patch('builtins.input', side_effect=[4,1,5,6,7,8,9,3,2])
    def test_main(self,mock_stdout):
        a=main()
        self.assertEqual(a,"better luck next time, I HAVE WON")
    
    
        
        

        