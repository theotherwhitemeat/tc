"""
http://community.topcoder.com/stat?c=problem_statement&pm=6249
Problem Statement for Alignment

Problem Statement
 You are given two Strings: A and B. You would like to align these two strings by inserting '-' characters in them so that every character in A lines up with the same character in B or with a '-' in B, and vice versa. Each maximal sequence of consecutive '-' characters costs x, plus an additional 1 per each '-' character. For example, changing "ABC" to "A-B-C" costs x+1+x+1, while changing it to "A--BC" costs x+2. Given, A, B, and x return the minimum cost to align the two strings.
 
Definition
     
Class: Alignment
Method: align
Parameters: String, String, int
Returns: int
Method signature: int align(String A, String B, int x)
(be sure your method is public)
    
 
Constraints
- A and B each contain between 1 and 50 uppercase letters ('A'-'Z'), inclusive.
- x will be between 0 and 100, inclusive.
 
Examples
0) 
     
"ABC"
"ACE"
1
Returns: 4
We can line things up as:
ABC-
A-CE
1) 
     
"AAABAAAABAA"
"AAAABAABAAA"
1
Returns: 7
 AAA-BAAAABAA-
 AAAABAA--BAAA
2) 
     
"AAABAAAABAA"
"AAAABAABAAA"
10
Returns: 28
 AAABAAAABAA----
 AAA----ABAABAAA
3) 
     
"AA"
"B"
1
Returns: 5
"""

""" Status: WIP """

""" Implementation strategy:

So we can get the distance between the strings using my
terrible run-time implementation of:

  http://en.wikipedia.org/wiki/Levenshtein_distance

...but the weighting / cost needs to be calculated differently.

"""

class Alignment(object):
    def __init__(self):
        pass

    @staticmethod
    def align(a, b, x):
        """ (int) aligns strings A and B via '-' characters and returns alignment cost """

        resultA = str()
        resultB = str()

    @staticmethod
    def getStringCost(string, x):
        """ (int) given a string, calculate the total cost if '-' is cost x + 1 and
             and '--' is x + 2 """

        cost = 0
        dash = 0
        for char in string:
            if char == '-':
                dash += 1
            elif dash > 0:
                cost += (x + dash)
                dash = 0
        # now account for a string ending with dashes
        if dash > 0:
            cost += (x + dash)

        return cost

    @staticmethod
    def getRecStringCost(string, x, dash):
        """ (int) given a string, calculate the total cost if '-' is cost x + 1 and
             and '--' is x + 2, recursively """
        # return degenerate string case: empty
        if len(string) == 0 and dash:
            return x
        elif len(string) == 0:
            return 0
        else:
            cost = 0
            if dash and not(string[-1] == '-'): cost += x
            if string[-1] == '-': cost += 1
            dash = string[-1] == '-'
            return (Alignment.getRecStringCost(string[0:-1], x, dash) + cost)

    @staticmethod
    def verifyAlignment(a, b):
        """ (bool) verifies two strings are aligned """
        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
            return True
        else:
            return False

    @staticmethod
    def recursiveLevDistance(s, t):
        """ (int) Recursively calculates the Levenshtein distance between two strings """

        len_s = len(s)
        len_t = len(t)

        # test for degenerate cases of empty strings
        if (len_s == 0): return len_t
        if (len_t == 0): return len_s

        # test if last characters of the strings match
        if (s[len_s-1] == t[len_t-1]):
            cost = 0
        else:
            cost = 1

        return min(Alignment.recursiveLevDistance(s[0:len_s-1], t) + 1,
                   Alignment.recursiveLevDistance(s, t[0:len_t-1]) + 1,
                   Alignment.recursiveLevDistance(s[0:len_s-1], t[0:len_t-1]) + cost)
''' WIP
    @staticmethod
    def recWeightedLevDistance(s, t, x, dash):
        """ Recursively calculates the Levenshtein distance between two strings using
        a weighted methodology: '-' is x+1, '--' is x + 2 """

        len_s = len(s)
        len_t = len(t)

        # test for degenerate cases of empty strings
        if (len_s == 0): return Alignment.getStringCost(t)
        if (len_t == 0): return Alignment.getStringCost(s)

        # test if last characters of the strings match
        if (s[len_s-1] == t[len_t-1]):
            cost = 0
        else:
            cost = 1

        return min(Alignment.recWeightedLevDistance(s[0:len_s-1], t, x) + 1,
                   Alignment.recWeightedLevDistance(s, t[0:len_t-1], x) + 1,
                   Alignment.recWeightedLevDistance(s[0:len_s-1], t[0:len_t-1], x) + cost)
'''

def main():
    """ sup main """
    pass

if __name__ == "__main__":
    main()



