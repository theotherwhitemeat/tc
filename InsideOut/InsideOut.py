"""
http://community.topcoder.com/stat?c=problem_statement&pm=3452

Problem Statement for InsideOut
        
Your printer has been infected by a virus and is printing gibberish. After staring at several printed pages for a while, you realize that it is printing every line inside-out. In other words, the left half of each line is being printed starting in the middle of the page and proceeding out toward the left margin. Similarly, the right half of each line is being printed starting at the right margin and proceeding in toward the middle of the page. For example, the line

    THIS LINE IS GIBBERISH
is being printed as
    I ENIL SIHTHSIREBBIG S
Your task is to unscramble a String line from its printed form back into its original order. You can assume that line contains an even number of characters.
 
Definition
        
Class:  InsideOut
Method: unscramble
Parameters: String
Returns:    String
Method signature:   String unscramble(String line)
(be sure your method is public)
    
 
Constraints
-   line contains between 2 and 50 characters, inclusive.
-   line contains an even number of characters.
-   line contains only uppercase letters ('A'-'Z') and spaces (' ').
 
Examples
0)  
        
"I ENIL SIHTHSIREBBIG S"
Returns: "THIS LINE IS GIBBERISH"
The example above.
1)  
        
"LEVELKAYAK"
Returns: "LEVELKAYAK"
2)  
        
"H YPPAHSYADILO"
Returns: "HAPPY HOLIDAYS"
3)  
        
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Returns: "MLKJIHGFEDCBAZYXWVUTSRQPON"
4)  
        
"RUT OWT SNEH HCNERF EERHTEGDIRTRAP A DNA  SEVODELT"
Returns: "THREE FRENCH HENS TWO TURTLEDOVES  AND A PARTRIDGE"


Status: Complete
Runtime: O(n) where n == len(line)
"""

class InsideOut(object):
    def __init__(self):
        pass

    @staticmethod
    def unscramble(line):
        """ (string) Given a string, reverse the first half, then reverse and
            append the second half. """

        # Return the first half reversed + the second half reversed.
        #  First half: start in the middle, minus 1, then iterate backwards.
        #  Second half: start at the end, then iterate backwards to halfway.
        return line[len(line)/2-1::-1] + line[:len(line)/2-1:-1]

def main():
    """ sup main """
    
    tests = ["I ENIL SIHTHSIREBBIG S", "LEVELKAYAK", "H YPPAHSYADILO"
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             "RUT OWT SNEH HCNERF EERHTEGDIRTRAP A DNA  SEVODELT"]

    for test in tests:
        print "%s unscrambled: %s" % (test, InsideOut.unscramble(test))

if __name__ == "__main__":
    main()



