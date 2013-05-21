"""
http://community.topcoder.com/stat?c=problem_statement&pm=12297

Problem Statement for TypingDistance
        
Jakub is trying out a one-dimensional keyboard. It consists of a single row of keys. The distance between any two adjacent keys is 1. Each key contains a distinct letter of the English alphabet. Jakub uses only one finger to type on the keyboard. He wonders what is the smallest total distance he will have to move his finger while typing a given word.

For example, if the keyboard's only row is "qwertyuiop", and Jakub wants to type the word "potter", he will have to move his finger from 'p' to 'o' (distance 1), from 'o' to 't' (distance 4), from 't' to 't' (distance 0), from 't' to 'e' (distance 2) and from 'e' to 'r' (distance 1), for a total distance of 1 + 4 + 0 + 2 + 1 = 8.

You are given a String keyboard and a String word, describing the keyboard and the word Jakub wants to write. Return the minimum distance he will have to move his finger in order to type the word on the keyboard.
 
Definition
        
Class:  TypingDistance
Method: minDistance
Parameters: String, String
Returns:    int
Method signature:   int minDistance(String keyboard, String word)
(be sure your method is public)
    
 
Notes
-   When moving the finger from the i-th key to the j-th key, the distance covered by the move can be computed as |i-j|, that is, the positive difference between i and j.
 
Constraints
-   keyboard will contain between 1 and 26 characters, inclusive.
-   Each character in keyboard will be a different lowercase letter of the English alphabet ('a'-'z').
-   word will contain between 1 and 50 characters, inclusive.
-   Each character in word will be present in keyboard.
 
Examples
0)  
        
"qwertyuiop", "potter"
Returns: 8
The example from the problem statement.
1)  
        
"tc", "tctcttccctccccttc"
Returns: 9
2)  
        
"a", "aaaaaaaaaaa"
Returns: 0
3)  
        
"kwadrutove", "rowerowe"
Returns: 39
4)  
        
"qwertyuiopasdfghjklzxcvbnm", "topcodersingleroundmatchgoodluckhavefun"
Returns: 322

Status: Complete
Runtime: O(n + m) where n == len(keyboard), m == len(word)
"""

class TypingDistance(object):
    def __init__(self):
        pass

    @staticmethod
    def minDistance(keyboard, word):
        """ (int) Given keyboard and word, determine the total distance
            some cat using a single-row keyboard would move their finger.
            This keyboard sounds terrible. """

        distance = int()
        keys = dict()

        # Create positional lookup dictionary for keys and their column index
        for i, key in enumerate(keyboard):
            keys[key] = i

        # Add up the distance
        for i, char in enumerate(word):
            if i != 0:
                distance += abs(keys[last_char] - keys[char])
            last_char = char

        return distance


def main():
    """ sup main """
    
    tests = [("qwertyuiop", "potter"),
             ("tc", "tctcttccctccccttc"),
             ("a", "aaaaaaaaaaa"),
             ("kwadrutove", "rowerowe"),
             ("qwertyuiopasdfghjklzxcvbnm",
                "topcodersingleroundmatchgoodluckhavefun")]

    for test in tests:
        print "keyboard, word: %s, %s" % (test[0], test[1])
        print "  Score: %d" % TypingDistance.minDistance(*test)


if __name__ == "__main__":
    main()
