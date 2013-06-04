"""
http://community.topcoder.com/stat?c=problem_statement&pm=6072

Problem Statement for Snowflakes
        
Paper snowflakes make great decorations and they are easy to make. Take a sheet of square checkered paper with an even number of squares on each side. Fold it in half, folding the upper part up and over to the bottom part, so that you have a rectangle. Now fold that rectangle in half lengthwise, from left to right, to make a smaller square. Next, take the right upper corner of that square and fold it up and over to the left bottom corner, forming a triangle (see pictures below, cells which stay immovable after all foldings are marked red on the fifth picture). Cut out some squares along grid lines (as shown on the last picture).

You will be given a String[] snowflake where each element represents a single row of squares in the folded pattern (the last picture shown above). The elements in snowflake are ordered from top row to bottom row, and each row is ordered from left to right. '*' represents a cut out square, and '.' represents an intact square. Unfold the triangle by reversing the steps described above. Return this flared out snowflake as a String[] of '.' and '*' characters. You should return the contents of the entire square even if the cut out cells split the snowflake into non-connected parts.

 
Definition
        
Class:  Snowflakes
Method: flareOut
Parameters: String[]
Returns:    String[]
Method signature:   String[] flareOut(String[] snowflake)
(be sure your method is public)
    
 
Constraints
-   snowflake will contain between 1 and 50 elements, inclusive.
-   The ith element of snowflake (0-indexed) will contain exactly i+1 characters.
-   Each element of snowflake will contain only characters '*' or '.'.
 
Examples
0)  
        
[".",
 "..",
 "*.*"]
Returns: ["*.**.*", "......", "*....*", "*....*", "......", "*.**.*" ]
1)  
        
["*",
 "..",
 ".*.",
 ".**.",
 ".*.**"]
Returns: 
["**.*..*.**",
"*.**..**.*",
".*.*..*.*.",
"***....***",
"....**....",
"....**....",
"***....***",
".*.*..*.*.",
"*.**..**.*",
"**.*..*.**" ]
2)  
        
[".",
 "..",
 "***"]
Returns: ["******", "*....*", "*....*", "*....*", "*....*", "******" ]
3)  
        
["*",
 ".*",
 "***"]
Returns: ["******", "**..**", "*.**.*", "*.**.*", "**..**", "******" ]
4)  
        
[".",
 "..",
 "***",
 "...."]
Returns: 
["........",
".******.",
".*....*.",
".*....*.",
".*....*.",
".*....*.",
".******.",
"........" ]


Status: Complete
Runtime: O(n) where n is the total number of characters in the snowflake
"""

class Snowflakes(object):
    def __init__(self):
        pass

    @staticmethod
    def flareOut(snowflake):
        """ (string) Given a pattern applied to a folded piece of paper,
            return the pattern that the paper would produce when unfolded.
             """

        # Strategy:
        # 1) Unfold initial triangle
        # 2) Unfold horizontally left to right
        # 3) Unfold vertically top to bottom

        # Get width of the triangle base
        snow_w = len(snowflake[-1])

        # Unfold initial triangle, populating the missing places in the row
        #  using the following method: row n, index m should be filled using
        #  the character in row m, index n.
        for i, row in enumerate(snowflake):
            while len(row) < snow_w:
                row += snowflake[len(row)][i]
            # Unfold the paper horizontally, left to right using the following
            #  method: row n = (reverse of row n + row n)  
            snowflake[i] = row[::-1] + row

        # Unfold the paper vertically, top to bottom using the following
        #  method: mirror the bottom rows on top.
        snowflake = snowflake[::-1] + snowflake

        return snowflake


def main():
    """ sup main """
    
    tests = [[".", "..", "*.*"],
             ["*", "..", ".*.", ".**.", ".*.**"],
             [".", "..", "***"],
             ["*", ".*", "***"],
             [".", "..", "***", "...."]]

    for test in tests:
        print "Initial triangle:"
        for row in test:
            print row
        print "\nSnowflake:"
        for row in Snowflakes.flareOut(test):
            print row
        print '-----------------------------'


if __name__ == "__main__":
    main()



