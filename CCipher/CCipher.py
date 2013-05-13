"""
http://community.topcoder.com/stat?c=problem_statement&pm=1667

Problem Statement for CCipher
        
Julius Caesar used a system of cryptography, now known as Caesar Cipher, which shifted each letter 2 places further through the alphabet (e.g. 'A' shifts to 'C', 'R' shifts to 'T', etc.). At the end of the alphabet we wrap around, that is 'Y' shifts to 'A'.

We can, of course, try shifting by any number. Given an encoded text and a number of places to shift, decode it.

For example, "TOPCODER" shifted by 2 places will be encoded as "VQREQFGT". In other words, if given (quotes for clarity) "VQREQFGT" and 2 as input, you will return "TOPCODER". See example 0 below.

Definition
        
Class:  CCipher
Method: decode
Parameters: String, int
Returns:    String
Method signature:   String decode(String cipherText, int shift)
(be sure your method is public)
    
 
Constraints
-   cipherText has between 0 to 50 characters inclusive
-   each character of cipherText is an uppercase letter 'A'-'Z'
-   shift is between 0 and 25 inclusive
 
Examples
0)  
        
"VQREQFGT", 2
Returns: "TOPCODER"
1)  
        
"ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10
Returns: "QRSTUVWXYZABCDEFGHIJKLMNOP"
2)  
        
"TOPCODER", 0
Returns: "TOPCODER"
3)  
        
"ZWBGLZ", 25
Returns: "AXCHMA"
4)  
        
"DBNPCBQ", 1
Returns: "CAMOBAP"
5)  
        
"LIPPSASVPH", 4
Returns: "HELLOWORLD"


Status: Complete
Runtime: O(n)
"""

class CCipher(object):
    def __init__(self):
        pass

    @staticmethod
    def decode(cipherText, shift):
        """ (string) Given cipherText and shift, returns a decoded
            message.  Shift is done by: shift 1 would turn 'B' to 'A' """

        import string
        alphabet = string.uppercase
        decode_return = str()

        # setup two-way dictionary where 0:'A', 'A':0, 1:'B', 'B':1, etc
        alphadict = dict()
        for i, alpha in enumerate(alphabet):
            alphadict[i] = alpha
            alphadict[alpha] = i

        # get char's num, mod 26 to deal with negatives, then shift
        for char in cipherText:
            char_num = (alphadict[char] - shift) % 26
            decode_return += alphadict[char_num]

        return decode_return


def main():
    """ sup main """
    
    tests = [("VQREQFGT", 2),
             ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10),
             ("TOPCODER", 0),
             ("ZWBGLZ", 25),
             ("DBNPCBQ", 1),
             ("LIPPSASVPH", 4)]

    for test in tests:
        print "%s shifted %s: %s" % (test[0], test[1], CCipher.decode(*test))

if __name__ == "__main__":
    main()



