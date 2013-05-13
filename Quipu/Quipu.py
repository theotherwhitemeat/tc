"""
http://community.topcoder.com/stat?c=problem_statement&pm=1686

Problem Statement for Quipu
        
The Incas used a sophisticated system of record keeping consisting of bundles of knotted cords. Such a bundle of cords is called a quipu. Each individual cord represents a single number. Surprisingly, the Incas used a base-10 positional system, just like we do today. Each digit of a number is represented by a cluster of adjacent knots, with spaces between neighboring clusters. The digit is determined by the number of knots in the cluster. For example, the number 243 would be represented by a cord with knots tied in the following pattern

     -XX-XXXX-XXX-
where each uppercase 'X' represents a knot and each '-' represents an unknotted segment of cord (all quotes for clarity only).
Unlike many ancient civilizations, the Incas were aware of the concept of zero, and used it in their quipus. A zero is represented by a cluster containing no knots. For example, the number 204003 would be represented by a cord with knots tied in the following pattern

     -XX--XXXX---XXX-
        ^^    ^^^
        ^^    ^^^
        ^^    two zeros between these three segments
        ^^
        one zero between these two segments
Notice how adjacent dashes signal the presence of a zero.
Your task is to translate a single quipu cord into an integer. The cord will be given as a String knots containing only the characters 'X' and '-'. There will be a single '-' between each cluster of 'X's, as well as a leading '-' and a trailing '-'. The first cluster will not be empty.

 
Definition
        
Class:  Quipu
Method: readKnots
Parameters: String
Returns:    int
Method signature:   int readKnots(String knots)
(be sure your method is public)
    
 
Constraints
-   knots contains between 3 and 50 characters, inclusive.
-   knots contains only the characters 'X' and '-'. Note that 'X' is uppercase.
-   The first and last characters of knots are '-'s. The second character is 'X'.
-   knots does not contain 10 consecutive 'X's.
-   knots will represent a number between 1 and 1000000, inclusive.
 
Examples
0)  
        
"-XX-XXXX-XXX-"
Returns: 243
The first example above.
1)  
        
"-XX--XXXX---XXX-"
Returns: 204003
The second example above.
2)  
        
"-X-"
Returns: 1
3)  
        
"-X-------"
Returns: 1000000
4)  
        
"-XXXXXXXXX--XXXXXXXXX-XXXXXXXXX-XXXXXXX-XXXXXXXXX-"
Returns: 909979

Status: Complete
Runtime: O(n)
"""

class Quipu(object):
    def __init__(self):
        pass

    @staticmethod
    def readKnots(knots):
        """ (int) Given a knot configuration, returns the count """

        knot_count = int()
        dash_count = int()
        number = str() # use a string to setup return number

        # truncate leading and trailing dash
        knots = knots[1:-1]

        for item in knots:
            # add up the number of characters, then append them
            #  once the character run is complete
            if item == 'X':
                # if dash_count is non-zero, then add in the
                #  zeros to the number string
                if dash_count != 0:
                    number += '0' * (dash_count - 1)
                    dash_count = 0
                knot_count += 1
            else:  # else it's a dash
                if knot_count != 0:
                    number += str(knot_count)
                    knot_count = 0
                dash_count += 1
        # handle any remaining character runs
        if dash_count > 0:
            number += '0' * (dash_count -1)
        elif knot_count > 0:
            number += str(knot_count)

        return int(number)


def main():
    """ sup main """
    
    tests = ["-XX-XXXX-XXX-",
             "-XX--XXXX---XXX-",
             "-X-",
             "-X-------",
             "-XXXXXXXXX--XXXXXXXXX-XXXXXXXXX-XXXXXXX-XXXXXXXXX-"]

    for test in tests:
        print "Pattern %s equals: %d" % (test, Quipu.readKnots(test))

if __name__ == "__main__":
    main()



