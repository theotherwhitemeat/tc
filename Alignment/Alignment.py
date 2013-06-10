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
     
("ABC",
"ACE",
1)
Returns: 4
We can line things up as:
ABC-
A-CE
1) 
     
("AAABAAAABAA",
"AAAABAABAAA",
1)
Returns: 7
 AAA-BAAAABAA-
 AAAABAA--BAAA
2) 
     
("AAABAAAABAA",
"AAAABAABAAA",
10)
Returns: 28
 AAABAAAABAA----
 AAA----ABAABAAA
3) 
     
("AA", "B", 1)
Returns: 5
"""

""" Status: WIP """

""" Implementation strategy:

So we can get the distance between the strings using my
terrible run-time implementation of:

  http://en.wikipedia.org/wiki/Levenshtein_distance

...but the weighting / cost needs to be calculated differently.

"""

class Alignment(object):
    def __init__(self):
        pass

    @staticmethod
    def align(A, B, x):
        """ Given strings A, B, and cost x, calculate the minimally
             expensive string permutations. """

        def permute(index, p1, p2, dash):
            """ Given an index and two strings, permute them with dashes.
                Assumes index is apropos. """

            perm1 = p1[:i] + dash + p1[i:]
            perm2 = p2[:i] + dash + p2[i:]

            #print "Generated:\n%s\n%s\n\n%s\n%s" % (p1, perm2, perm1, p2)

            return [(p1, perm2), (perm1, p2)]

        def expense(p1, p2, x, dash):
            """ Given strings p1, p2, and expense i, calculate the total
                string costs.  Aggregate cost is calcuated by counting
                the number of dashes in each string and summing them.
                Additionally each unique run of dashes in a given string
                adds a cost of i. """

            p1run = False
            p2run = False
            cost = 0

            for i in range(len(p1)):
                if p1[i] == dash:
                    cost += 1
                    p1run = True
                elif p1run:
                    cost += x
                    p1run = False
            for i in range(len(p2)):
                if p2[i] == dash:
                    cost += 1
                    p2run = True
                elif p2run:
                    cost += x
                    p2run = False
            if p1run:
                cost += x
            if p2run:
                cost += x

            return cost

        i = 0
        pairs = list()
        finals = list()
        maxlen = len(A) * 2
        mincost = None
        pairs.append((A, B, i))
        dash = '-'

        # While there are still pairs to process...
        while len(pairs) > 0:
            p1, p2, i = pairs.pop(0)
            len1 = len(p1)
            len2 = len(p2)
            # Bail out if string is ever half or more dashes
            if max(len1, len2) >= maxlen:
                continue
            # Bail out if strings are already too expensive
            if (mincost is not None) and (expense(p1, p2, x, dash) >= mincost):
                continue
            #print "Popped: %s, %s, i = %d" % (p1, p2, i)

            # If string lengths are the same and i is past string len,
            #  the strings are fully processed.
            if (len1 == len2) and (len1 <= i):
                paircost = expense(p1, p2, x, dash)
                if (paircost < mincost) or mincost is None:
                    mincost = paircost
                    finals.append((p1, p2))
                    print "Finals: %s, %s" % (p1, p2)
                else:  # too expensive, move on
                    continue
            # p1 or p2 needs trailing dashes
            elif (len1 > len2) and i >= len2:
                p2 += dash
                pairs.append((p1, p2, i + 1))
            elif (len1 < len2) and i >= len1:
                p1 += dash
                pairs.append((p1, p2, i + 1))
            # If i'th char is the same, move ahead
            elif (p1[i] == p2[i]) or dash in (p1[i], p2[i]):
                pairs.append((p1, p2, i + 1))
                new_pairs = permute(i, p1, p2, dash)
                for p1, p2 in new_pairs:
                    pairs.append((p1, p2, i + 1))
            elif p1[i] != p2[i]:  # ...chars not equal, so permute
                new_pairs = permute(i, p1, p2, dash)
                for p1, p2 in new_pairs:
                    pairs.append((p1, p2, i + 1))

        return min([(expense(k[0], k[1], x, dash), k) for k in finals])


def main():
    """ sup main """
    
    tests = [("ABC", "ACE", 1),
             ("AAABAAAABAA", "AAAABAABAAA", 1),
             ("AAABAAAABAA", "AAAABAABAAA", 10),
             ("AA", "B", 1)]

    for test in tests:
        print "Given %s, smallest alignment: %s" % (test, Alignment.align(*test))

if __name__ == "__main__":
    main()



