"""
http://community.topcoder.com/stat?c=problem_statement&pm=2002

Problem Statement for WordForm


Problem Statement
        
In English, the letters A, E, I, O and U are the vowels. Y is also considered to be a vowel if it's not preceded by another vowel and is not the first letter in a word (the fact that a vowel is defined to some extent in terms of itself does not make it ambiguous). If a letter is not a vowel then it is a consonant. So in "TOY" the consonants are T and Y, and in "SYZYGY" they are S, Z and G.

A sequence of vowels will be denoted by uppercase letter 'V' and a sequence of consonants will be denoted by uppercase letter 'C'. A word can then be described as an alternating sequence of 'C' and 'V'. For instance, the word "WHEREABOUTS" has the sequence CVCVCVC, and the words "YORK" and "TOY" both have the sequence CVC. It's not permissible to have two or more consecutive 'V' or 'C' in the sequence.

Create a class WordForm containing the method getSequence which takes a String word and returns a String containing the word's sequence as described above. The word may contain both uppercase and lowercase letters, but your method should be case insensitive (see example 2).

 
Definition
        
Class:  WordForm
Method: getSequence
Parameters: String
Returns:    String
Method signature:   String getSequence(String word)
(be sure your method is public)
    
 
Notes
-   word may not be an English word, or a word in any language at all, but you should still use the rules defined above. See example 3.
 
Constraints
-   word will contain between 1 and 50 characters, inclusive.
-   word will only contain the characters 'A'-'Z' and 'a'-'z', both inclusive.
 
Examples
0)  
        
"WHEREABOUTS"
Returns: "CVCVCVC"
Here we have consonant-consonant-vowel-consonant-vowel-vowel-consonant-vowel-vowel-consonant-consonant. Putting together consecutive consonants and vowels gives us CVCVCVC.
1)  
        
"yoghurt"
Returns: "CVCVC"
2)  
        
"YipPy"
Returns: "CVCV"
Mixing lowercase and uppercase does not affect the result.
3)  
        
"AyYyEYye"
Returns: "VCVCVCV"
Even though this isn't an English word, we use the rules defined in the statement to find the consonant-vowel pattern.
4)  
        
"yC"
Returns: "C"


Status: Complete
Runtime: O(n) where n == len(word)
"""

class WordForm(object):
    def __init__(self):
        pass

    @staticmethod
    def getSequence(word):
        """ Given a word, return the consonant-vowel sequence
            using C and V, respectively. """

        # We'll construct our structure in sequence, and store
        #  info about last character, consonant runs, and vowel runs.
        sequence = str()
        c_run = bool()
        v_run = bool()
        word = word.lower()

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for i, char in enumerate(word):
            # Handle vowels with y corner-cases.
            #  If 'y' and preceded by a consonant, or a pure vowel
            if (c_run and char == 'y') or (char in vowels):
                # Account for the consonant run
                if c_run:
                    sequence += 'C'
                    c_run = False
                v_run = True
            # Else char is a consonant
            else:
                # Account for the vowel run
                if v_run:
                    sequence += 'V'
                    v_run = False
                c_run = True
        # Now account for the last character in the loop
        sequence += 'C' if c_run else 'V'

        return sequence

def main():
    """ sup main """
    
    tests = ["WHEREABOUTS", "yoghurt", "YipPy", "AyYyEYye", "yC"]

    for test in tests:
        print "Word: %s\n\tPattern: %s" % (test, WordForm.getSequence(test))

if __name__ == "__main__":
    main()



