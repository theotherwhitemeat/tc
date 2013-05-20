"""
http://community.topcoder.com/stat?c=problem_statement&pm=2268

Problem Statement for KiloMan
        
You've reached one of the last bosses in the new hit 2-D side-scrolling action game, KiloMan. The boss has a large gun that can shoot projectiles at various heights. For each shot, KiloMan can either stand still or jump. If he stands still and the shot is at height 1 or 2, then he gets hit. If he jumps and the shot is at a height above 2, then he is also hit. Otherwise, he is not hit. Given the height of each shot and a sequence of jumps, how many hits will KiloMan take?

The input int[] pattern is the pattern of heights at which the shots are being fired. Each element of pattern will be between 1 and 7, inclusive. The input String jumps is the sequence of jumps that KiloMan will attempt; 'J' means he will jump and 'S' means he will stand still. For example, if element 0 of pattern is 3 and character 0 of jumps is 'J', then KiloMan will jump right as a shot is fired at height 3 (and thus he will be hit).

Your method should return an int representing the number of times KiloMan is hit.

 
Definition
        
Class:  KiloMan
Method: hitsTaken
Parameters: int[], String
Returns:    int
Method signature:   int hitsTaken(int[] pattern, String jumps)
(be sure your method is public)
    
 
Constraints
-   pattern will contain between 1 and 50 elements, inclusive.
-   each number in pattern will be between 1 and 7, inclusive.
-   the number of characters in jumps will be the same as the number of elements in pattern
-   each character of jumps will be either 'S' or 'J'.
 
Examples
0)  
        
[1,3,2,3,3,1,2,2,1]
"JJSSSJSSJ"
Returns: 4
The first shot is at height 1, and KiloMan jumps it successfully. Then he jumps into a shot at height 3. KiloMan takes three more hits while standing against shots at height 2.
1)  
        
[1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,
 4,4,4,5,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,7]
"SSSSSSSSSSSSSSJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ"
Returns: 49
KiloMan stands still at all the wrong times and jumps at all the wrong times, taking all 49 hits.
2)  
        
[1,2,2,1]
"SJJS"
Returns: 2
Since everything was shot at height 2 or less, he should have jumped everything.
3)  
        
[1]
"J"
Returns: 0


Status: Complete
Runtime: O(n) where n == len(pattern)
"""

class KiloMan(object):
    def __init__(self):
        pass

    @staticmethod
    def hitsTaken(pattern, jumps):
        """ (int) Given a shot pattern and jump pattern, calculate the number
            of hits KiloMan will sustain. """

        hits = int()
        # Setup heights for which KiloMan is hit while standing or jumping
        stand_max = 2
        jump_min = 3

        for shot, jump in zip(pattern, jumps):
            if jump == 'J':
                # If shot height hits during a jump, increment hits
                if shot >= jump_min:
                    hits += 1
            if jump == 'S':
                # If shot height hits during standing, increment hits
                if shot <= stand_max:
                    hits += 1

        return hits


def main():
    """ sup main """
    
    tests = [([1,3,2,3,3,1,2,2,1],
               "JJSSSJSSJ"),
             ([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,
               4,4,4,5,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,7],
               "SSSSSSSSSSSSSSJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ"),
             ([1,2,2,1], "SJJS"),
             ([1], "J")]

    for test in tests:
        print "Shots: %s\nJumps: %s\nHits: %d\n" % (test[0],
                                                    test[1],
                                                    KiloMan.hitsTaken(*test))


if __name__ == "__main__":
    main()
