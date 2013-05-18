"""
http://community.topcoder.com/stat?c=problem_statement&pm=4788

Problem Statement for CheckFunction

You are given a String code containing a message composed entirely of decimal digits ('0'-'9'). Each digit consists of some number of dashes (see diagram below). A "check function" of a message is defined as the total number of dashes in the message. Return the value of the check function for the message represented in code.

Definition
        
Class:  CheckFunction
Method: newFunction
Parameters: String
Returns:    int
Method signature:   int newFunction(String code)
(be sure your method is public)
    
 
Notes
-   0 consists of 6 dashes, 1 consists of 2 dashes, 2 consists of 5 dashes, 3 consists of 5 dashes, 4 consists of 4 dashes, 5 consists of 5 dashes, 6 consists of 6 dashes, 7 consists of 3 dashes, 8 consists of 7 dashes, 9 consists of 6 dashes.
 
Constraints
-   code will contain between 1 and 50 characters, inclusive.
-   Each character in code will be a digit ('0'-'9').
 
Examples
0)  
        
"13579"
Returns: 21
1 consists of 2 dashes;

3 consists of 5 dashes;

5 consists of 5 dashes;

7 consists of 3 dashes;

9 consists of 6 dashes;

2 + 5 + 5 + 3 + 6 = 21.
1)  
        
"02468"
Returns: 28
2)  
        
"73254370932875002027963295052175"
Returns: 157

Status: Complete
Runtime: O(n), where n = number of characters
"""

class CheckFunction(object):
    def __init__(self):
        pass

    @staticmethod
    def newFunction(code):
        """ (int) Given code which is a string of numbers, return the number of
            dashes each character in the string would contain, in total. """

        total = int()
        vals = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

        for char in code:
            # cast char to integer value, then lookup the dashes for int val
            total += vals[int(char)]

        return total

def main():
    """ sup main """
    
    tests = ["13579", "02468", "73254370932875002027963295052175"]

    for test in tests:
        print "%s dash count: %d" % (test, CheckFunction.newFunction(test))

if __name__ == "__main__":
    main()



