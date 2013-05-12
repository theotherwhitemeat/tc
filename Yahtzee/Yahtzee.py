"""
http://community.topcoder.com/stat?c=problem_statement&pm=1692

Problem Statement for Yahtzee
        
This task is about the scoring in the first phase of the die-game Yahtzee, where five dice are used. The score is determined by the values on the upward die faces after a roll. The player gets to choose a value, and all dice that show the chosen value are considered active. The score is simply the sum of values on active dice.

Say, for instance, that a player ends up with the die faces showing 2, 2, 3, 5 and 4. Choosing the value two makes the dice showing 2 active and yields a score of 2 + 2 = 4, while choosing 5 makes the one die showing 5 active, yielding a score of 5.

Your method will take as input an int[] toss, where each element represents the upward face of a die, and return the maximum possible score with these values.

 
Definition
        
Class:  Yahtzee
Method: maxPoints
Parameters: int[]
Returns:    int
Method signature:   int maxPoints(int[] toss)
(be sure your method is public)
    
 
Constraints
-   toss will contain exactly 5 elements.
-   Each element of toss will be between 1 and 6, inclusive.
 
Examples
0)  
        
[ 2, 2, 3, 5, 4 ]
Returns: 5
The example from the text.
1)  
        
[ 6, 4, 1, 1, 3 ]
Returns: 6
Selecting 1 as active yields 1 + 1 = 2, selecting 3 yields 3, selecting 4 yields 4 and selecting 6 yields 6, which is the maximum number of points.
2)  
        
[ 5, 3, 5, 3, 3 ]
Returns: 10


Status: Complete
Runtime: O(n)
"""

class Yahtzee(object):
    def __init__(self):
        pass

    @staticmethod
    def maxPoints(toss):
        """ (int) Returns the maximum score from a given yahtzee roll.
            Scoring is done by adding up all equivalent integers, thus
            a roll with 2x 2's will score 4. """

        rolls = dict()

        # Add up the rolls: {roll_num: total_roll_score}
        for roll in toss:
            rolls[roll] = rolls.get(roll, 0) + roll

        return max(rolls.values())

def main():
    """ sup main """
    
    tests = [[ 2, 2, 3, 5, 4 ],
             [ 6, 4, 1, 1, 3 ],
             [ 5, 3, 5, 3, 3 ],]

    for test in tests:
        print "Roll %s max points: %d" % (test, Yahtzee.maxPoints(test))

if __name__ == "__main__":
    main()



