"""
http://community.topcoder.com/stat?c=problem_statement&pm=12438

Problem Statement for FoxAndGame

Fox Ciel is playing the popular game 'Cut the Rope' on her smartphone. The game has multiple stages, and for each stage the player can gain between 0 and 3 stars, inclusive. You are given a String[] result containing Fox Ciel's current results: For each stage, result contains an element that specifies Ciel's result in that stage. More precisely, result[i] will be "---" if she got 0 stars in stage i, "o--" if she got 1 star, "oo-" if she got 2 stars and "ooo" if she managed to get all 3 stars. Return the total number of stars Ciel has at the moment.
 
Definition
        
Class:  FoxAndGame
Method: countStars
Parameters: String[]
Returns:    int
Method signature:   int countStars(String[] result)
(be sure your method is public)
    
 
Constraints
-   result will contain between 1 and 50 elements, inclusive.
-   Each element in result will be one of "---", "o--", "oo-", "ooo".
 
Examples
0)  
        
["ooo",
 "ooo"]
Returns: 6
There are two stages. In each of them, Ciel got all three stars. Together, she now has 3+3 = 6 stars.
1)  
        
["ooo",
 "oo-",
 "o--"]
Returns: 6
This time the answer is 3 + 2 + 1 = 6.
2)  
        
["ooo",
 "---",
 "oo-",
 "---",
 "o--"]
Returns: 6
3)  
        
["o--",
 "o--",
 "o--",
 "ooo",
 "---"]
Returns: 6
4)  
        
["---",
 "o--",
 "oo-",
 "ooo",
 "ooo",
 "oo-",
 "o--",
 "---"]
Returns: 12
5)  
        
["---",
 "---",
 "---",
 "---",
 "---",
 "---"]
Returns: 0
6)  
        
["oo-"]
Returns: 2


Status: Complete
Runtime: O(n) where n is the total number of characters in result
"""

class FoxAndGame(object):
    def __init__(self):
        pass

    @staticmethod
    def countStars(result):
        """ (int) Count the 'o's in the strings from the list passed in. """

        stars = int()

        # Iterate through each character from each string and += stars for o's
        for row in result:
            for char in row:
                if char == 'o':
                    stars += 1

        return stars

def main():
    """ sup main """
    
    tests = [(["ooo",
             "ooo"]),
             (["ooo",
             "oo-",
             "o--"]),
             (["ooo",
             "---",
             "oo-",
             "---",
             "o--"]),
             (["o--",
             "o--",
             "o--",
             "ooo",
             "---"]),
             (["---",
             "o--",
             "oo-",
             "ooo",
             "ooo",
             "oo-",
             "o--",
             "---"]),
             (["---",
             "---",
             "---",
             "---",
             "---",
             "---"]),
             (["oo-"]),
              ]

    for test in tests:
        for row in test: print row
        print "Stars: %d" % FoxAndGame.countStars(test)

if __name__ == "__main__":
    main()



