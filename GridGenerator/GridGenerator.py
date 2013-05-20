"""
http://community.topcoder.com/stat?c=problem_statement&pm=4688

Problem Statement for GridGenerator

Consider the following grid of numbers:
 1 0  3  4   1
 4 5  8  15  20
 1 10 23 46  81
 0 11 44 113 240
 3 14 69 226 579

Aside from the top row and left column, each number is equal to the sum of the three numbers immediately left, above, and above-left of it. You will be given a int[], row, representing the first row of a similar grid, and a int[], col, representing the first column of the grid. Your task is to return the value of the lower rightmost location when the values are calculated in the same way. Hence, the above example would be represented by the input row = [1,0,3,4,1],, col = [1,4,1,0,3],.
 
Definition
        
Class:  GridGenerator
Method: generate
Parameters: int[], int[]
Returns:    int
Method signature:   int generate(int[] row, int[] col)
(be sure your method is public)
    
 
Constraints
-   row and col will contain the same number of elements.
-   row and col will contain between 2 and 10 elements, inclusive.
-   Each element of row and col will be between 0 and 9, inclusive.
-   The first element of row will be the same as the first element of col.
 
Examples
0)  
        
[1,0,3,4,1],
[1,4,1,0,3],
Returns: 579
The example above.
1)  
        
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
Returns: 13163067
The largest possible return.
2)  
        
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
Returns: 0

Status: Complete
Runtime: O(n^2) where n == len(row)
"""

class GridGenerator(object):
    def __init__(self):
        pass

    @staticmethod
    def generate(row, col):
        """ (int) Given a seed first row and first col, generate the remainder
             of a grid, then return the value in the bottom-right most cell.
             Cell values are calculated by adding the values of the number
             immediately left, above and above-left. """

        prev_row = row
        next_row = list()
        last_val = int()

        # Iterate through each starting row value in column, building out
        #  number values.
        for i, col_val in enumerate(col[1:]):
            # Append the first column value as the first item in the row
            next_row.append(col_val)
            # Iterate through row range starting from the second element,
            #  building out number values
            for k in range(1, len(row)):
                next_row.append(next_row[-1] + prev_row[k] + prev_row[k-1])
            # Set the last value to return, every time because it's cheaper
            #  than a conditional that you check every time plus an assignment
            #  although I guess that depends on how the compiler works, but 
            #  I digress.  Roll next_row back to prev_row.
            last_val = next_row[-1]
            prev_row = next_row
            next_row = list()

        return last_val


def main():
    """ sup main """
    
    tests = [([1,0,3,4,1],
              [1,4,1,0,3]),
             ([9,9,9,9,9,9,9,9,9,9],
              [9,9,9,9,9,9,9,9,9,9]),
             ([0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0])]

    for test in tests:
        # Print outline of what grid looks like: first row, then first column.
        print "Template: \n%s" % ' '.join([str(derp) for derp in test[0]])
        for row in test[1][1:]:
            print row
        print "Last value: %d" % GridGenerator.generate(*test)


if __name__ == "__main__":
    main()
