"""
http://community.topcoder.com/stat?c=problem_statement&pm=2923

Problem Statement for TallPeople

A group of people stand before you arranged in rows and columns. Looking from above, they form an R by C rectangle of people. You will be given a String[] people containing the height of each person. Elements of people correspond to rows in the rectangle. Each element contains a space-delimited list of integers representing the heights of the people in that row. Your job is to return 2 specific heights in a int[]. The first is computed by finding the shortest person in each row, and then finding the tallest person among them (the "tallest-of-the-shortest"). The second is computed by finding the tallest person in each column, and then finding the shortest person among them (the "shortest-of-the-tallest").
 
Definition
        
Class:  TallPeople
Method: getPeople
Parameters: String[]
Returns:    int[]
Method signature:   int[] getPeople(String[] people)
(be sure your method is public)

Constraints
-   people will contain between 2 and 50 elements inclusive.
-   Each element of people will contain between 3 and 50 characters inclusive.
-   Each element of people will be a single space-delimited list of positive integers such that: 

1) Each positive integer is between 1 and 1000 inclusive with no extra leading zeros.

2) Each element contains the same number of integers.

3) Each element contains at least 2 positive integers.

4) Each element does not contain leading or trailing whitespace.
 
Examples
0)  
        
["9 2 3",
 "4 8 7"]
Returns: [ 4,  7 ]
The heights 2 and 4 are the shortest from the rows, so 4 is the taller of the two. The heights 9, 8, and 7 are the tallest from the columns, so 7 is the shortest of the 3.
1)  
        
["1 2",
 "4 5",
 "3 6"]
Returns: [ 4,  4 ]
2)  
        
["1 1",
 "1 1"]
Returns: [ 1,  1 ]


Status: Complete
Runtime: O(n*m) where n = row and m = column
"""

class TallPeople(object):
    def __init__(self):
        pass

    @staticmethod
    def getPeople(people):
        """ (int) Given a list of strings of people heights, return
            the tallest of the shortest in each row and the shortest
            of the tallest in each column. """

        # row heights as a list, col heights as a dict so we can index []
        row_heights = list()
        col_heights = dict()

        for row in people:
            row_shortest = 0
            for k, column in enumerate(row):
                # skip blank chars
                if column == ' ': continue
                # find the shortest entry in the row
                if (int(column) < row_shortest) or (row_shortest == 0):
                    row_shortest = int(column)
                # find shortest entry in the column
                if int(column) > col_heights.get(k, 0):
                    col_heights[k] = int(column)
            # append shortest row entry
            row_heights.append(row_shortest)

        print max(row_heights), min(col_heights.values())


def main():
    """ sup main """
    
    tests = [(["9 2 3",
               "4 8 7"]),
             (["1 2",
               "4 5",
               "3 6"]),
             (["1 1",
               "1 1"])]

    for test in tests:
        TallPeople.getPeople(test)

if __name__ == "__main__":
    main()



