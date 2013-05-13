"""
http://community.topcoder.com/stat?c=problem_statement&pm=1962

Problem Statement for PassingGrade
        
You are studying for the final exam in a tough course, and want to know how many points you need to score on the final to pass the course. You know how many points you earned on each assignment (pointsEarned), how many points were possible on each assignment (pointsPossible), and how many points are possible on the final exam (finalExam). You need to earn a minimum of 65% of the total possible points to pass the course. Assume your score on the final exam will be an integral number of points between 0 and finalExam, inclusive. Return the number of points you need to score on the final to pass the course, or -1 if it is impossible for you to pass the course.

 
Definition
        
Class:  PassingGrade
Method: pointsNeeded
Parameters: int[], int[], int
Returns:    int
Method signature:   int pointsNeeded(int[] pointsEarned, int[] pointsPossible, int finalExam)
(be sure your method is public)
    
 
Constraints
-   pointsEarned contains between 1 and 20 elements, inclusive.
-   pointsPossible contains the same number of elements as pointsEarned.
-   Each element of pointsPossible is between 1 and 1000, inclusive.
-   Element i of pointsEarned is between 0 and element i of pointsPossible, inclusive.
-   finalExam is between 1 and 3000, inclusive.
 
Examples
0)  
        
[55,77,82,60],
[100,100,100,100],
300
Returns: 181
If you score 181 points on the final, then you will finish the course with exactly 65% of the possible points.
1)  
        
[ 1, 2, 3, 4 ],
[ 2, 3, 4, 5 ],
7
Returns: 4
If you score 4 points on the final, then you pass with 66.7% of the total possible points, but if you score 3 points on the final, then you fail with 61.9% of the possible points.
2)  
        
[ 1, 2, 2, 1 ],
[ 9, 9, 9, 9 ],
9
Returns: -1
Even if you score 9 points on the final, you still fail with 33.3% of the possible points.
3)  
        
[ 7, 8, 7, 6 ],
[ 8, 8, 8, 8 ],
9
Returns: 0
You will pass even if you score 0 points on the final.
4)  
        
[ 17, 23, 50, 200, 19, 56, 83, 91, 77, 9, 0 ],
[ 20, 30, 50, 250, 20, 70, 100, 100, 100, 10, 10 ],
400
Returns: 129
5)  
        
[600,600,600,600,600,600,600,600,600,600,
 600,600,600,600,600,600,600,600,600,600],
[1000,1000,1000,1000,1000,1000,1000,1000,
 1000,1000,1000,1000,1000,1000,1000,1000,
 1000,1000,1000,901],
3000
Returns: 2886


Status: Complete
Runtime: O(n)
"""

class PassingGrade(object):
    def __init__(self):
        pass

    @staticmethod
    def pointsNeeded(pointsEarned, pointsPossible, finalExam):
        """ (int) Given points earned on assignments, points possible 
             per assignment and the max score on a final exam, Returns
             the grade necessary on the final exam to pass with a 65% """

        import math

        # setup total points earned, possible, needed, and what the 
        #  student needs on the exam to pass
        total_earned = sum(pointsEarned)
        total_possible = sum(pointsPossible) + finalExam
        total_needed = math.ceil(total_possible * 0.65) # round up
        exam_needed = total_needed - total_earned
        # setup return value
        exam_return = int()

        # return 0 if student doesn't need any points, -1 if it's impossible
        #  or the value they need if possible to pass with a 65%
        if exam_needed <= 0:
            exam_return = 0
        elif exam_needed > finalExam:
            exam_return = -1
        else:
            exam_return = exam_needed

        return exam_return

def main():
    """ sup main """
    
    tests = [([55,77,82,60],
            [100,100,100,100],
            300),
             ([ 1, 2, 3, 4 ],
            [ 2, 3, 4, 5 ],
            7),
             ([ 1, 2, 2, 1 ],
            [ 9, 9, 9, 9 ],
            9),
             ([ 7, 8, 7, 6 ],
            [ 8, 8, 8, 8 ],
            9),
             ([ 17, 23, 50, 200, 19, 56, 83, 91, 77, 9, 0 ],
            [ 20, 30, 50, 250, 20, 70, 100, 100, 100, 10, 10 ],
            400),
             ([600,600,600,600,600,600,600,600,600,600,
             600,600,600,600,600,600,600,600,600,600],
            [1000,1000,1000,1000,1000,1000,1000,1000,
             1000,1000,1000,1000,1000,1000,1000,1000,
             1000,1000,1000,901],
            3000),]

    for test in tests:
        print "Score needed: %d" % (PassingGrade.pointsNeeded(*test))

if __name__ == "__main__":
    main()



