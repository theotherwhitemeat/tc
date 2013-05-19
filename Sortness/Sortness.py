"""
http://community.topcoder.com/stat?c=problem_statement&pm=7263

Problem Statement for Sortness

The sortness of a sequence of distinct numbers is the average of the sortness of each element. The sortness of an element is the number of higher elements that come before it in the sequence plus the number of lower elements that come after it in the sequence. The lower the sortness of a sequence, the closer it is to being sorted. Only a sorted sequence has a sortness of 0.

For example, in the sequence [3,2,1,4,6,7,5,8] the numbers 1,2,3 and 5 have a sortness of 2, numbers 6 and 7 have a sortness of 1 and numbers 4 and 8 have a sortness of 0. The sortness of the sequence is the average of all those sortness values: (2+2+2+2+1+1+0+0)/8 = 1.25.

You will be given a sequence of distinct numbers a as a int[]. Return the sortness of a.

 
Definition
        
Class:  Sortness
Method: getSortness
Parameters: int[]
Returns:    double
Method signature:   double getSortness(int[] a)
(be sure your method is public)
    
 
Constraints
-   a will contain between 1 and 50 elements, inclusive.
-   a will contain exactly one occurrence of each integer between 1 and the number of elements in a, inclusive.
 
Examples
0)  
        
[3,2,1,4,6,7,5,8]
Returns: 1.25
The example in the problem statement.
1)  
        
[1,2,3]
Returns: 0.0
A sorted sequence has a sortness of zero.
2)  
        
[5,4,3,2,1]
Returns: 4.0
A reversed sequence has maximum sortness.
3)  
        
[1,5,8,7,9,6,10,12,11,3,4,2]
Returns: 5.166666666666667


Status: Complete
Runtime: O(n^2), where n is number of elements passed in.  This could
  probably be optimized.
"""

class Sortness(object):
    def __init__(self):
        pass

    @staticmethod
    def getSortness(a):
        """ (float) Given a sequence of numbers, return the sortness
             defined as the average of the sortness of each element.  The
             sortness of an element is defined as how many places out of 
             order the element is, thus [1,2,3] has a sortness of zero 
             while [3,2,1] has a sortness of (2 + 0 + 2) / 3 == 1.3333 """

        off_sort = int()

        # Iterate through a, finding items that are out of sort
        for i, num in enumerate(a):
            sortness = int()
            # Compare each number to all of the other elements
            for k, num_compare in enumerate(a):
                # If num_compare is more than num and comes before num
                if int(num_compare) > int(num) and k < i:
                    sortness += 1
                # If num_compare is less than num and comes after num
                elif int(num_compare) < int(num) and k > i:
                    sortness += 1
            off_sort += sortness

        # Return average sortness, dividing by the number of items in a
        return off_sort / float(len(a))


def main():
    """ sup main """
    
    tests = [[3,2,1,4,6,7,5,8],
             [1,2,3],
             [5,4,3,2,1],
             [1,5,8,7,9,6,10,12,11,3,4,2]]

    for test in tests:
        print "Sortness of %s:\n %f \n" % (test, Sortness.getSortness(test))


if __name__ == "__main__":
    main()
