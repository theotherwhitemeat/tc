"""
http://community.topcoder.com/stat?c=problem_statement&pm=8204

Problem Statement for WhiteCells
        
A chessboard is an 8 x 8 grid of cells. Within each column and within each row, cells alternate between black and white. The cell in the upper left corner (0, 0) is white. You are given a String[] board, where the j-th character of the i-th element is 'F' if the cell in the j-th column from the left and i-th row from the top is occupied, or '.' if it is empty. Return the number of occupied white cells on the board.

 
Definition
        
Class:  WhiteCells
Method: countOccupied
Parameters: String[]
Returns:    int
Method signature:   int countOccupied(String[] board)
(be sure your method is public)
    
 
Constraints
-   board will contain exactly 8 elements.
-   Each element of board will contain exactly 8 characters.
-   board will contain only the characters '.' and 'F'.
 
Examples
0)  
        
["........",
 "........",
 "........",
 "........",
 "........",
 "........",
 "........",
 "........"]
Returns: 0
1)  
        
["FFFFFFFF",
 "FFFFFFFF",
 "FFFFFFFF",
 "FFFFFFFF",
 "FFFFFFFF",
 "FFFFFFFF",
 "FFFFFFFF",
 "FFFFFFFF"]
Returns: 32
2)  
        
[".F.F...F",
 "F...F.F.",
 "...F.F.F",
 "F.F...F.",
 ".F...F..",
 "F...F.F.",
 ".F.F.F.F",
 "..FF..F."]
Returns: 1
3)  
        
["........",
 "..F.....",
 ".....F..",
 ".....F..",
 "........",
 "........",
 ".......F",
 ".F......"]
Returns: 2


Status: Complete
Runtime: O(n) where n is the total number of spaces on the chessboard, so this will 
  always be 64 unless someone, like, redefines chess.
"""

class WhiteCells(object):
    def __init__(self):
        pass

    @staticmethod
    def countOccupied(board):
        """ (int) Given a board (consisting of a list of strings showing cell
            occupancy which we define as '.' for unoccupied, and 'F' for
            occupied), count the total number of occupied white cells """

        white_cells = int()

        # Walk through cells, recording white occupancy which we define as [i+k] % 2
        for i, row in enumerate(board):
            for k, cell in enumerate(row):
                if cell == 'F' and (((i + k) % 2) == 0):
                    white_cells += 1

        return white_cells


def main():
    """ sup main """
    
    tests = [(["........",
             "........",
             "........",
             "........",
             "........",
             "........",
             "........",
             "........"]),
            (["FFFFFFFF",
             "FFFFFFFF",
             "FFFFFFFF",
             "FFFFFFFF",
             "FFFFFFFF",
             "FFFFFFFF",
             "FFFFFFFF",
             "FFFFFFFF"]),
            ([".F.F...F",
             "F...F.F.",
             "...F.F.F",
             "F.F...F.",
             ".F...F..",
             "F...F.F.",
             ".F.F.F.F",
             "..FF..F."]),
            (["........",
             "..F.....",
             ".....F..",
             ".....F..",
             "........",
             "........",
             ".......F",
             ".F......"])]

    for test in tests:
        for row in test: print row
        print "Occupied white cells: %d \n" % (WhiteCells.countOccupied(test))

if __name__ == "__main__":
    main()
