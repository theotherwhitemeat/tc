"""
http://community.topcoder.com/stat?c=problem_statement&pm=11471

Problem Statement for LargestSubsequence
        
For Strings x and y, we say y is a subsequence of x if y can be obtained from x by erasing some (possibly all or none) of the letters in x. For example, "tpcdr" is a subsequence of "topcoder", while "rt" is not.

Given a String s, return the lexicographically largest subsequence of s.

 
Definition
        
Class:  LargestSubsequence
Method: getLargest
Parameters: String
Returns:    String
Method signature:   String getLargest(String s)
(be sure your method is public)
    
 
Notes
-   For strings x and y, x is said to be lexicographically larger than y if y is a prefix of x or y has a smaller character than x at the first position where they differ. Order of characters is defined as the order of ASCII codes: 'a' < 'b' < ... < 'z'.
 
Constraints
-   s will contain between 1 and 50 characters, inclusive.
-   Each character in s will be a lowercase letter ('a'-'z').
 
Examples
0)  
        
"test"
Returns: "tt"
All subsequences listed in lexicographical order are "" (empty string), "e", "es", "est", "et", "s", "st", "t", "te", "tes", "test", "tet", "ts", "tst" and "tt". So return "tt".
1)  
        
"a"
Returns: "a"
There are only two subsequences, "" and "a".
2)  
        
"example"
Returns: "xple"
3)  
        
"aquickbrownfoxjumpsoverthelazydog"
Returns: "zyog"

Status: WIP
Runtime: 
"""

class LargestSubsequence(object):
    def __init__(self):
        pass

    @staticmethod
    def getLargest(s):
        """ (str()) Given string s, return the lexicographically largest
            subsequence. """

        #Strategy: generate all substrings, then rank them

        def generateSubstrings(string_base):
            """ () Given a string base, generate all possible substrings. """

            # Strategy: creating a counting bit mask to reference string 
            #  positions, and use that to generate the substrings:
            #  abc
            #  001: c
            #  010: b
            #  011: bc

            for i in range(len(string_base)):
                print bin(i)

        generateSubstrings(s)

        

def main():
    """ sup main """
    
    tests = ["test", "a", "example", "aquickbrownfoxjumpsoverthelazydog"]

    for test in tests:
        print "Substrings-%s: %s" % (test, LargestSubsequence.getLargest(test))

if __name__ == "__main__":
    main()



