"""
http://community.topcoder.com/stat?c=problem_statement&pm=1835

Problem Statement for Poetry
        
Given a poem, determine its rhyme scheme.

To simplify things, because English is such a fickle language, there are some constraints:

A legal word is a sequence of lower or uppercase letters, containing at least one vowel, where a vowel is 'a', 'e', 'i', 'o', or 'u'. Also, 'y' is considered a vowel if it is not at the start or end of a word. Words are delimited by spaces.

Two words are considered rhyming if they have the same ending pattern (defined below). This comparison is case-insensitive (see Example 1.)

An ending pattern is a substring of a word such that:

The word ends with that substring,
The substring contains exactly one contiguous string of vowels,
The first letter of the substring is a vowel, and
The substring must either be the whole string, or the letter immediately preceding the start of the substring must be a nonvowel.
For example, the ending pattern of "bought" is "ought", the ending pattern of "spying" would be "ying", and the ending pattern of "all" would be "all". (Note that "spy" has no vowels, and thus is not a legal word.)

Two lines rhyme if their corresponding last words rhyme, and a line is empty if it contains no words.

The procedure for determinining rhyme scheme is as follows: The first non-empty line in the poem should be labeled with the lowercase letter 'a'. Every line that rhymes with that line should also be labeled with that letter. The next unlabeled non-empty line should be labeled with the letter 'b', and any rhyming lines should also be labeled in this manner. When you run out of lowercase letters, continue by using the uppercase letters 'A' to 'Z'. Empty lines should be labeled with ' ' (the space character).

The 0th character of the returned String should be the rhyme scheme label of the 0th line, the 1st character should be the label of the 1st line, and so on. This means that the returned String will have the same number of characters as there are elements in poem. Thus, given a String[] poem, then your method should return a String detailing the rhyme scheme.

 
Definition
        
Class:  Poetry
Method: rhymeScheme
Parameters: String[]
Returns:    String
Method signature:   String rhymeScheme(String[] poem)
(be sure your method is public)
    
 
Notes
-   If there is a blank line in the poem, there must be a corresponding space in the output. A blank line is one with no words. (See Example 1.)
 
Constraints
-   poem will have between 1 and 50 elements, inclusive.
-   each element of poem will contain between 0 and 50 characters, inclusive.
-   the only allowable characters in poem will be upper and lowercase characters ('a'-'z' and 'A'-'Z') and the space character (' ').
-   there will be only legal words in poem
 
Examples
0)  
        
["I hope this problem",
 "is a whole lot better than",
 "this stupid haiku"],
Returns: "abc"
Doesn't even conceivably rhyme.
1)  
        
["     ",
 "Measure your height",
 "AND WEIGHT      ",
 "said the doctor",
 "",
 "And make sure to take your pills",
 "   to   cure   your    ills",
 "Every",
 "DAY"],
Returns: " aab ccde"
Even though "height" and "weight" don't actually rhyme in English, they do by the rules laid out above.
2)  
        
["One bright day in the middle of the night",
 "Two dead boys got up to fight",
 "Back to back they faced each other",
 "Drew their swords and shot each other",
 "",
 "A deaf policeman heard the noise",
 "And came to arrest the two dead boys",
 "And if you dont believe this lie is true",
 "Ask the blind man he saw it too"],
Returns: "aabb cdef"
3)  
        
["",
 "",
 "",
 ""],
Returns: "    "
Four lines from the mind of a blank poet.
4)  
        
["This poem has uppercase letters",
 "In its rhyme scheme",
 "Alpha", "Blaster", "Cat", "Desert", "Elephant", "Frog", "Gulch", 
 "Horse", "Ireland", "Jam", "Krispy Kreme", "Loofah", "Moo", "Narf",
 "Old", "Pink", "Quash", "Rainbow", "Star", "Tour", "Uvula", "Very",
 "Will", "Xmas", "Young", "Zed", "deception", "comic", "grout",
 "oval", "cable", "rob", "steal", "steel", "weak"],
Returns: "abcdefghibjkblmnopqrstcuvwxyzABCbDEFG"
5)  
        
[" ",
 "     ",
 "This poem",
 "         ",
 " ",
 " ",
 "",
 "Has lots of blank lines",
 " ",
 "      ",
 "                                            ",
 "         ",
 " ",
 "              ",
 "                                                  ",
 "  in      it           "],
Returns: "  a    b       c"
6)  
        
["too bad   your",
 "     solution went   sour"],
Returns: "aa"

Status: Complete
Runtime: O(poem_lines * avg_word_letters)
"""

class Poetry(object):
    def __init__(self):
        pass

    @staticmethod
    def rhymeScheme(poem):
        """ (string) Given a list of lines (poem), return the rhyme scheme """

        import string

        def getRhymeSubStr(werd):
            """ (string) finds and returns rhyming substring of a word """
            # step through werd in reverse order
            substr = str()
            vowel_run = False
            for letter in werd[::-1]:
                # break if we've found a vowel run, and it's over
                if vowel_run and letter not in vowels:
                    break
                if letter == 'y' and vowel_run:
                    break
                if letter in vowels:
                    vowel_run = True
                substr += letter
            # reverse the order back and return
            return substr[::-1]

        scheme_return = str()
        vowels = set(['a','e','i','o','u','y'])
        rhymers_and_labels = dict()
        rhymers = set()  # for a faster lookup
        labels = string.lowercase + string.uppercase
        
        for line in poem:
            # convert to lowercase as we're case insensitive
            words = line.strip().lower().split()
            # handle degenerate case: no words in line
            if len(words) == 0:
                scheme_return += ' '
            else:
                # get the last word, then find the rhyme substr
                last_word = words[-1]
                rhymer = getRhymeSubStr(last_word)
                # determine if we've used this rhymer before
                if rhymer in rhymers:
                    scheme_return += rhymers_and_labels[rhymer]
                else:
                    # pop off a new label from labels
                    label, labels = labels[0], labels[1:]
                    # add rhyming substr to dict and set, update scheme
                    rhymers_and_labels[rhymer] = label
                    rhymers.add(rhymer)
                    scheme_return += label

        return scheme_return


def main():
    """ sup main """
    
    tests = [(["I hope this problem",
               "is a whole lot better than",
               "this stupid haiku"],),
            (["     ",
             "Measure your height",
             "AND WEIGHT      ",
             "said the doctor",
             "",
             "And make sure to take your pills",
             "   to   cure   your    ills",
             "Every",
             "DAY"],),
            (["One bright day in the middle of the night",
             "Two dead boys got up to fight",
             "Back to back they faced each other",
             "Drew their swords and shot each other",
             "",
             "A deaf policeman heard the noise",
             "And came to arrest the two dead boys",
             "And if you dont believe this lie is true",
             "Ask the blind man he saw it too"],),
            (["",
             "",
             "",
             ""],),
            (["This poem has uppercase letters",
             "In its rhyme scheme",
             "Alpha", "Blaster", "Cat", "Desert", "Elephant", "Frog", "Gulch", 
             "Horse", "Ireland", "Jam", "Krispy Kreme", "Loofah", "Moo", "Narf",
             "Old", "Pink", "Quash", "Rainbow", "Star", "Tour", "Uvula", "Very",
             "Will", "Xmas", "Young", "Zed", "deception", "comic", "grout",
             "oval", "cable", "rob", "steal", "steel", "weak"],),
            ([" ",
             "     ",
             "This poem",
             "         ",
             " ",
             " ",
             "",
             "Has lots of blank lines",
             " ",
             "      ",
             "                                            ",
             "         ",
             " ",
             "              ",
             "                                                  ",
             "  in      it           "],),
            (["too bad   your",
             "     solution went   sour"],),]

    for test in tests:
        print Poetry.rhymeScheme(*test)

if __name__ == "__main__":
    main()



