"""
http://community.topcoder.com/stat?c=problem_statement&pm=6635

Problem Statement for RosePetals

"Petals Around the Rose" is a pretty well known logic game. A person who knows the game rolls five dice and then says a number. The other players must guess the rule used to obtain that number. We will not ask you to play this game because it's a tricky one. We will simply tell you that the rule is to sum the number of dots that are around the center dot of each die, like the petals around a rose. If a die has no dot in the center, it has no petals. The face of the die labeled with 1 dot has 0 petals, the face with 2 dots has 0 petals, the face with 3 dots has 2 petals, the face with 4 dots has 0 petals, the face with 5 dots has 4 petals and finally the face with 6 dots has 0 petals as can be seen in the picture.

You are given a int[] dice containing the values of the five dice. Return the total number of petals in this configuration.
 
Definition
        
Class:  RosePetals
Method: getScore
Parameters: int[]
Returns:    int
Method signature:   int getScore(int[] dice)
(be sure your method is public)
    
 
Constraints
-   dice will contain exactly 5 elements.
-   Each element of dice will be between 1 and 6, inclusive.
 
Examples
0)  
        
[1, 2, 3, 2, 1]
Returns: 2
In this case we have 0 petals for 1 as there are no dots around the central dot, 0 petals for 2 as it has no central dot, 2 petals for 3, 0 petals for 2 and 0 petals for 1.
1)  
        
[4, 4, 5, 6, 5]
Returns: 8
In this case we have 0 petals + 0 petals + 4 petals + 0 petals + 4 petals = 8 petals.
2)  
        
[1, 2, 3, 3, 5]
Returns: 8
3)  
        
[3, 3, 3, 3, 3]
Returns: 10
4)  
        
[2, 2, 2, 2, 2]
Returns: 0


Status: Complete
Runtime: O(n) where n == len(dice) 
"""

class RosePetals(object):
    def __init__(self):
        pass

    @staticmethod
    def getScore(dice):
        """ (int) Given some dice, count the dots about the middle. """

        petal_count = int()
        rose_petals = {1:0, 2:0, 3:2, 4:0, 5:4, 6:0}

        for roll in dice:
            petal_count += rose_petals[roll]

        return petal_count

def main():
    """ sup main """
    
    tests = [[1, 2, 3, 2, 1], [4, 4, 5, 6, 5], [1, 2, 3, 3, 5],
              [3, 3, 3, 3, 3], [2, 2, 2, 2, 2]]

    for test in tests:
        print "Petal count of %s: %d" % (test, RosePetals.getScore(test))

if __name__ == "__main__":
    main()



