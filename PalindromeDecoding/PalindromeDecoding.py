"""
http://community.topcoder.com/stat?c=problem_statement&pm=6767

Problem Statement for PalindromeDecoding

You are given a String code and int[]s position and length. code contains an encoded string which you must decode using the following method. Step through the elements of position in order, and for each element i, take the substring of length length[i] at position position[i]. Insert the reverse of that substring before position position[i]+length[i], thereby creating a palindromic substring. All positions are 0-based. Return the decoded String.
 
Definition
        
Class:  PalindromeDecoding
Method: decode
Parameters: String, int[], int[]
Returns:    String
Method signature:   String decode(String code, int[] position, int[] length)
(be sure your method is public)
    
 
Constraints
-   code will contain between 1 and 10 characters, inclusive.
-   code will contain only digits ('0'-'9') and letters ('a'-'z', 'A'-'Z').
-   position will contain between 0 and 10 elements, inclusive.
-   length will contain the same number of elements as position.
-   position and length will always refer to a valid substring in the (partially decoded) string code.
-   Each element of length will be positive.
-   The return value will have at most 1000 characters.
 
Examples
0)  
        
"ab",
[0],
[2],
Returns: "abba"
The decoding step selects the whole string and appends it in reversed form.
1)  
        
"Misip",
[2,3,1,7],
[1,1,2,2],
Returns: "Mississippi"
The decoding steps are: "Misip" -> "Missip" -> "Misssip" -> "Mississip" -> "Mississippi"
2)  
        
"XY",
[0, 0, 0, 0],
[2, 4, 8, 16],
Returns: "XYYXXYYXXYYXXYYXXYYXXYYXXYYXXYYX"
In this example the length of the string doubles in each decoding step.
3)  
        
"TC206",
[1,2,5],
[1,1,1],
Returns: "TCCC2006"
4)  
        
"nodecoding"
[],
[],
Returns: "nodecoding"


Status: Complete
Runtime: O(m*2^n) where m = len(code) and n = len(position)
"""

class PalindromeDecoding(object):
    def __init__(self):
        pass

    @staticmethod
    def decode(code, position, length):
        """ (str()) Given an encoded string, and a list of positions and lengths,
             decode the string using the methodology described above. """

        # Concat from code[0] to code[num[i] + length[i]], then the reverse of
        #  code[num[i]] to code[num[i] + length[i]], then the remainder of the
        #  encoded string: from code[num[i] + length[i]] to code[end].
        for i, num in enumerate(position):
            code = code[:num+length[i]] + code[num:length[i]+num][::-1] + code[num+length[i]:]

        return code

def main():
    """ sup main """
    
    tests = [("ab", [0], [2]),
             ("Misip", [2,3,1,7], [1,1,2,2]),
             ("XY", [0, 0, 0, 0], [2, 4, 8, 16]),
             ("TC206", [1,2,5], [1,1,1]),
             ("nodecoding", [], [],)]

    for test in tests: 
        print "Decoded %s: %s" % (test[0], PalindromeDecoding.decode(*test))

if __name__ == "__main__":
    main()



