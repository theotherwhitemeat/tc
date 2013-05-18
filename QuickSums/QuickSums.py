"""
http://community.topcoder.com/stat?c=problem_statement&pm=2829

Problem Statement for QuickSums

Given a string of digits, find the minimum number of additions required for the string to equal some target number. Each addition is the equivalent of inserting a plus sign somewhere into the string of digits. After all plus signs are inserted, evaluate the sum as usual. For example, consider the string "12" (quotes for clarity). With zero additions, we can achieve the number 12. If we insert one plus sign into the string, we get "1+2", which evaluates to 3. So, in that case, given "12", a minimum of 1 addition is required to get the number 3. As another example, consider "303" and a target sum of 6. The best strategy is not "3+0+3", but "3+03". You can do this because leading zeros do not change the result.
Write a class QuickSums that contains the method minSums, which takes a String numbers and an int sum. The method should calculate and return the minimum number of additions required to create an expression from numbers that evaluates to sum. If this is impossible, return -1.
 
Definition
        
Class:  QuickSums
Method: minSums
Parameters: String, int
Returns:    int
Method signature:   int minSums(String numbers, int sum)
(be sure your method is public)
    
 
Constraints
-   numbers will contain between 1 and 10 characters, inclusive.
-   Each character in numbers will be a digit.
-   sum will be between 0 and 100, inclusive.
 
Examples
0)  
        
"99999"
45
Returns: 4
In this case, the only way to achieve 45 is to add 9+9+9+9+9. This requires 4 additions.
1)  
        
"1110"
3
Returns: 3
Be careful with zeros. 1+1+1+0=3 and requires 3 additions.
2)  
        
"0123456789"
45
Returns: 8
3)  
        
"99999"
100
Returns: -1
4)  
        
"382834"
100
Returns: 2
There are 3 ways to get 100. They are 38+28+34, 3+8+2+83+4 and 3+82+8+3+4. The minimum required is 2.
5)  
        
"9230560001"
71
Returns: 4

Status: Complete
Runtime: O(2^(n-1))
  I believe this runtime is 2 to the power of n-1.  The number of permutations to generate doubles with 
  each addition character, thus we see:

    String "1" results in a single permutation (2^0): 1
    String "11" results in 2 permutations (2^1): 1, 1+1
    String "111" results in 4 permutations (2^2): 111, 11+1, 1+11, 1+1+1
"""

class QuickSums(object):
    def __init__(self):
        pass

    @staticmethod
    def minSums(numbers, num_sum):
        """ (int) Given a string of numbers, return the minimum number of additions
            necessary to transform the numbers to the target sum.  Example: given
            string "33" and sum 6, the string should be "3+3" and thus will return 1. """

        def generate_permutations(numbers):
            """ [string,] Given a string of numbers, generate all possible permutations
                of the numbers with plusses in between.  "1" returns "1".
                "11" returns ["11", "1+1"], etc """

            permutations = list()
            temp = list()
            # Generate all possible permutations of numbers and plusses, record
            #  the number of plus signs as cost.
            for i, num in enumerate(numbers):
                # Base case, append the number and cost of 0
                if i == 0:
                    permutations.append((num, 0))
                else:
                    # Iterate through permutations, appending new items to temp.
                    #  Strings can be permutated two ways: string + char,
                    #                                      string + '+' + char
                    for item in permutations:
                        temp.append((item[0] + num, item[1]))
                        temp.append((item[0] + '+' + num, item[1] + 1))
                    # Now we move temp to permutations and clear out temp.
                    permutations = temp
                    temp = list()
            return permutations

        def clean_eval(exp):
            """ (int) Evaluate expression, ensuring we account for weirdness with
                leading zeros, etc. """

            # Split expression using '+' as our split token
            number_string = exp.split("+")
            total = int()

            # Cost each number string to int, cleaning up leading zeros, then total
            for num in number_string:
                total += int(num)

            return total

        # Create a dictionary of each permutations' sum and cost.  Cost is defined as
        #  the total number of additions necessary to generate the sum.
        value_costs = dict()

        # Iterate through permutations and populate values and their
        #  respective costs into value_costs.  If we find two equal values
        #  with differing costs, use the lower cost.
        for perm in generate_permutations(numbers):
            value = clean_eval(perm[0])
            cost = perm[1]
            # Default the cost to 20 as an upper limit, given our number
            #  will never cost more than 9 given 10 characters max.
            if value_costs.get(value, 20) > cost:
                value_costs[value] = cost

        return value_costs.get(num_sum, -1)


def main():
    """ sup main """
    
    tests = [("99999", 45),
             ("1110", 3),
             ("0123456789", 45),
             ("99999", 100),
             ("382834", 100),
             ("9230560001", 71),]

    for test in tests:
        print "Nums: %s, Target: %d, Additions: %s" % (test[0],
                                                       test[1],
                                                       QuickSums.minSums(*test))

if __name__ == "__main__":
    main()



