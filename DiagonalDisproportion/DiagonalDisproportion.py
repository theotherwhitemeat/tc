"""
http://community.topcoder.com/stat?c=problem_statement&pm=6003

Problem Statement for DiagonalDisproportion

You are to calculate the diagonal disproportion of a square matrix. The diagonal disproportion of a square matrix is the sum of the elements of its main diagonal minus the sum of the elements of its collateral diagonal. The main and collateral diagonals of a square matrix are shown in figures 1 and 2 respectively.

The elements of the main diagonal are shown in green in figure 1, and the elements of the collateral diagonal are shown in cyan in figure 2.

Given a String[] matrix, return its diagonal disproportion. The j'th character of the i'th element of matrix should be treated as the element in the i'th row and j'th column of the matrix.

 
Definition
        
Class:  DiagonalDisproportion
Method: getDisproportion
Parameters: String[]
Returns:    int
Method signature:   int getDisproportion(String[] matrix)
(be sure your method is public)
    
 
Constraints
-   matrix will contain between 1 and 50 elements, inclusive.
-   Each element of matrix will contain only digits ('0'-'9').
-   The number of characters in each element of matrix will be equal to the number of elements in matrix.
 
Examples
0)  
        
["190","828","373"]
Returns: 1
The sum of the elements of the main diagonal is 1+2+3 = 6. The sum of the elements of the collateral diagonal is 0+2+3 = 5. So, the answer is 6-5 = 1.
1)  
        
["9000","0120","0000","9000"]
Returns: -1
2)  
        
["6"]
Returns: 0
The matrix has only one element, and this element lies on both the main and collateral diagonals.
3)  
        
["7748297018","8395414567","7006199788","5446757413","2972498628",
"0508396790","9986085827","2386063041","5687189519","7729785238"]
Returns: -24

Status: Complete
Runtime: O(n) where n is matrix height (or width, it's the same)
"""

class DiagonalDisproportion(object):
    def __init__(self):
        pass

    @staticmethod
    def getDisproportion(matrix):
        """ (int) Given a list of strings, which should be interpreted as a matrix,
            calculate and return the diagonal disproportion - defined as the sum of
            row[i],  col[i], minus the sum of row[i] and col[width-i] . """

        # Setup counters for main and collateral diagonals
        main = int()
        coll = int()
        matrix_width = len(matrix[0])

        # Add up main and collateral diagonal values, subtract 1 from width for
        #  zero-based indexing
        for i, row in enumerate(matrix):
            main += int(row[i])
            coll += int(row[matrix_width - i - 1])

        disproportion = main - coll

        return disproportion

def main():
    """ sup main """
    
    tests = [["190","828","373"],
             ["9000","0120","0000","9000"],
             ["6"],
             ["7748297018","8395414567","7006199788","5446757413","2972498628",
             "0508396790","9986085827","2386063041","5687189519","7729785238"]]

    for test in tests:
        print "%s \n Dispro: %d \n" % (test, DiagonalDisproportion.getDisproportion(test))

if __name__ == "__main__":
    main()



