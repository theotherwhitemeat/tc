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
     
"AAA  BAAAABAA"
"AAA ABAA  BAAA"
1
Returns: 7
 AAA-BAAAABAA-
 AAAABAA--BAAA
2) 
     
"AAA BAAAABAA"
"AAAABAA  BAAA"
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

(let's call this naive / brute-force?)
1) generate string permutations
2) calculate costs
	cost = dash + x
3) pick the cheapest
"""

class Alignment(object):
	def __init__(self):
		pass

	@staticmethod
	def align(A, B, x):
		""" (int) aligns strings A and B via '-' characters and returns alignment cost """

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


		resultA = str()
		resultB = str()


def main():
	""" sup main """


if __name__ == "__main__":
    main()