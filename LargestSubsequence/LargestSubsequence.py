"""
http://community.topcoder.com/stat?c=problem_statement&pm=11471

Problem Statement for LargestSubsequence
        
For Strings x and y, we say y is a subsequence of x if y can be obtained from x by erasing some (possibly all or none) of the letters in x. For example, "tpcdr" is a subsequence of "topcoder", while "rt" is not.

Given a String s, return the lexicographically largest subsequence of s.

 
Definition
        
Class:  LargestSubsequence
Method: getLargest
Parameters: String
Returns:    String
Method signature:   String getLargest(String s)
(be sure your method is public)
    
 
Notes
-   For strings x and y, x is said to be lexicographically larger than y if y is a prefix of x or y has a smaller character than x at the first position where they differ. Order of characters is defined as the order of ASCII codes: 'a' < 'b' < ... < 'z'.
 
Constraints
-   s will contain between 1 and 50 characters, inclusive.
-   Each character in s will be a lowercase letter ('a'-'z').
 
Examples
0)  
        
"test"
Returns: "tt"
All subsequences listed in lexicographical order are "" (empty string), "e", "es", "est", "et", "s", "st", "t", "te", "tes", "test", "tet", "ts", "tst" and "tt". So return "tt".
1)  
        
"a"
Returns: "a"
There are only two subsequences, "" and "a".
2)  
        
"example"
Returns: "xple"
3)  
        
"aquickbrownfoxjumpsoverthelazydog"
Returns: "zyog"

Status: Complete
Runtime: O(nlogn)
"""

class LargestSubsequence(object):
    def __init__(self):
        pass

    @staticmethod
    def getLargest(s):
        """ (str()) Given string s, return the lexicographically largest
            subsequence. """

        # Strategy
        #
        # Discussion:
        #  This method discovers the largest possible substring in a 
        #  given string.  The criteria are subtle, and the problem
        #  statement above must be read to understand this implementation.
        #
        #  The largest substring in string (s) is built by finding the largest
        #  lexico character (x) in string (s) iterating from left to right,
        #  and then the largest lexico character after (x), and so on.  For
        #  'abc' the largest character is the last, thus the largest substring
        #  is simply 'c'.  For 'zabcz', the largest lexico characters are the
        #  first and last, and thus the largest substring is 'zz'. Finally for
        #  string 'cba', the largest characters are in order, and thus the
        #  largest substring is 'cba'.
        #
        # Implementation:
        #  1) Push chars to priority queue, then pop into a sorted list.
        #  2a) Iterate through characters and append each character
        #   that is different from the previous and has a larger index.
        #  2b) Handle cases where the same character repeats multiple
        #   times and may or may not have an appropriate index to append.

        import Queue 
        import sys

        char_q = Queue.PriorityQueue()
        prioritized_chars = list()
        output = str()
        last_index = -1
        last_char = str()
        dupe_count = int()
        dupe_max = int()
        first_run = True

        # Push items to priority queue
        for i, char in enumerate(s):
            char_q.put((char, i))

        # Pop items off of priority queue to sort them
        while char_q.qsize() > 0:
            prioritized_chars.append(char_q.get())

        # Iterate through chars in order of largest first
        for next_char, next_index in prioritized_chars[::-1]:
            # Setup initial run characters
            if first_run:
                char = next_char
                index = next_index
                first_run = False
            else:
                # If the next char is different...
                if char != next_char:
                    # If this char and the last are the same, increase dupes
                    if (char == last_char) and (index > last_index):
                        dupe_count += 1
                    # If we have dupes, append them to output
                    if dupe_count > 0:
                        output += dupe_count * char
                        dupe_count = 0
                        last_index = dupe_max
                    # Else if this char isn't a dupe of the previous nor the
                    #  next, so it is unique and we may append it. Only append
                    #  if the index is larger than the previous, append it.
                    elif index > last_index:
                        output += char
                        last_index = index
                # If this char and the next char are the same...
                else:
                    # If this duplicate has a larger index, increase dupe count
                    if index > last_index:
                        print "Adding", 
                        dupe_count += 1
                        dupe_max = max(index, dupe_max)
                # Housekeeping: update last_char, char, index
                last_char = char
                char = next_char
                index = next_index
        # Handle the final case: if dupe, increase count
        if (char == last_char) and (index > last_index):
            dupe_count += 1
        # If dupe, append apropos chars
        if dupe_count > 0:
            output += dupe_count * char
        # If this isn't a dupe, and has a higher index, append char
        if (char != last_char) and (index > last_index):
            output += char

        return output


def main():
    """ sup main """
    
    tests = ["test", "a", "example", "aquickbrownfoxjumpsoverthelazydog"]

    for test in tests:
        print "Substrings-%s: %s" % (test, LargestSubsequence.getLargest(test))

if __name__ == "__main__":
    main()



