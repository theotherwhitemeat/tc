"""
http://community.topcoder.com/stat?c=problem_statement&pm=2911

Problem Statement for MatchMaking

Problem Statement

You are developing the matchmaking component of an online dating site. Prospective members must fill out a questionnaire consisting of binary questions such as Do you prefer to vacation (a) in the mountains or (b) at the seaside? and Would you rather travel (a) by plane or (b) by train?

You are to match up men with women by maximizing the number of answers each couple has in common. A man and a woman have an answer in common whenever they give the same answer to the same question. Conflicts can easily arise due to numerical ties, but you will be able to resolve all such conflicts using the following procedure. Note that there will be equal numbers of men and women, with names being unique in each sex.

Take the woman whose name comes earliest in lexicographic order, and consider the men with whom she has the greatest number of answers in common. Among these men, pick the one whose name comes earliest in lexicographic order. You have found the woman's best match. Remove this couple from the dating pool, and repeat the matching procedure until there are no more singles left.

You are given a String[], namesWomen, containing the names of single women, and another String[], answersWomen, containing their answers. The kth element of answersWomen lists the answers of the woman whose name is the kth element of namesWomen. If there are n questions in the questionnaire, then every element of answersWomen consists of n characters, each of which is either 'a' or 'b'. The answers are always given in the fixed questionnaire order. You are similarly given the String[]s namesMen and answersMen for the single men. Lastly, you are given a String, queryWoman, containing the name of a woman. Return the name of the man to whom she is matched after you have formed all couples according to the above rules.


Definition

Class:  MatchMaking
Method: makeMatch
Parameters: String[], String[], String[], String[], String
Returns:    String
Method signature:   String makeMatch(String[] namesWomen, String[] answersWomen, String[] namesMen, String[] answersMen, String queryWoman)
(be sure your method is public)

Notes
-   Lexicographic order is like dictionary order, with the difference that case matters. All uppercase letters take precedence over all lowercase letters. Thus, "boolean" comes before "boot"; "boo" comes before "boolean"; "Boot" comes before "boo"; "Zoo" comes before "boo".

Constraints
-   namesWomen contains between 1 and 50 elements, inclusive
-   if namesWomen consists of n elements, then answersWomen, namesMen, and answersMen consist of n elements each
-   each element of namesWomen and each element of namesMen is between 1 and 50 characters long, inclusive
-   the only characters that may appear in namesMen and namesWomen are 'a' to 'z' and 'A' to 'Z'
-   no two elements of namesWomen are alike
-   no two elements of namesMen are alike
-   the first element of answersWomen is between 1 and 50 characters long, inclusive
-   if the first element of answersWomen consists of m characters, then each element of answersWomen and of answersMen is m characters long
-   the only characters that may appear in answersWomen and answersMen are 'a' and 'b'
-   queryWoman is one of the Strings in namesWomen

Examples
0)

["Constance", "Bertha", "Alice"],
["aaba", "baab", "aaaa"],
["Chip", "Biff", "Abe"],
["bbaa", "baaa", "aaab"],
"Bertha"
Returns: "Biff"
Alice has two answers in common with Chip and three answers in common with both Abe and Biff; Abe gets lexicographic preference. Bertha also has two answers in common with Chip and three answers in common with both Abe and Biff. Since Abe has already been matched to Alice, Bertha lands Biff.
1)

["Constance", "Bertha", "Alice"],
["aaba", "baab", "aaaa"],
["Chip", "Biff", "Abe"],
["bbaa", "baaa", "aaab"],
"Constance"
Returns: "Chip"
We are dealing with the same names and answers as before. Constance is the last to go. Although she has two answers in common with Abe and Biff, they are both taken. She ends up with Chip, with whom she has only one answer in common.
2)

["Constance", "Alice", "Bertha", "Delilah", "Emily"],
["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
["Ed", "Duff", "Chip", "Abe", "Biff"],
["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
"Constance"
Returns: "Duff"
3)

["Constance", "Alice", "Bertha", "Delilah", "Emily"],
["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
["Ed", "Duff", "Chip", "Abe", "Biff"],
["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
"Delilah"
Returns: "Chip"
4)

["Constance", "Alice", "Bertha", "Delilah", "Emily"],
["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
["Ed", "Duff", "Chip", "Abe", "Biff"],
["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
"Emily"
Returns: "Ed"
5)

["anne", "Zoe"],
["a", "a"],
["bob", "chuck"],
["a", "a"],
"Zoe"
Returns: "bob"
6)

["F", "M", "S", "h", "q", "g", "r", "N", "U", "x", "H", "P",
 "o", "E", "R", "z", "L", "m", "e", "u", "K", "A", "w", "Q",
 "O", "v", "j", "a", "t", "p", "C", "G", "k", "c", "V", "B",
 "D", "s", "n", "i", "f", "T", "I", "l", "d", "J", "y", "b"],
["abaabbbb", "bbaabbbb", "aaabaaab", "aabbaaaa", "baabbaab",
 "aaababba", "bbabbbbb", "bbbabbba", "aaabbbba", "aabbbaaa",
 "abbabaaa", "babbabbb", "aaaaabba", "aaaabbaa", "abbbabaa",
 "babababa", "abbaaaaa", "bbababba", "baaaaaba", "baaaaabb",
 "bbbbabba", "ababbaaa", "abbbabab", "baabbbaa", "bbbaabbb",
 "aababbab", "ababbabb", "abbaabba", "baabbabb", "aaabaaab",
 "aabbbaba", "aabaaabb", "abababba", "aabbaaaa", "aabbabaa",
 "bababaaa", "aabaaaab", "bbbbaabb", "baaababb", "abaabbab",
 "aabbbaaa", "baabbaba", "bbabbbaa", "aabbbbaa", "abbbaaab",
 "abababbb", "ababaaba", "bababaaa"],
["f", "C", "v", "g", "Q", "z", "n", "c", "B", "o", "M", "F",
 "u", "x", "I", "T", "K", "L", "E", "U", "w", "A", "d", "t",
 "e", "R", "D", "s", "p", "q", "m", "r", "H", "j", "J", "V",
 "l", "a", "k", "h", "G", "y", "i", "P", "O", "N", "b", "S"],
["bbbaabab", "bbabaabb", "ababbbbb", "bbbababb", "baababaa",
 "bbaaabab", "abbabbaa", "bbbabbbb", "aabbabab", "abbababa",
 "aababbbb", "bababaab", "aaababbb", "baabbaba", "abaaaaab",
 "bbaababa", "babaabab", "abbabbba", "ababbbab", "baabbbab",
 "babbaaab", "abbbbaba", "bbabbbba", "baaabaab", "ababbabb",
 "abbbaabb", "bbbbaabb", "bbbaaabb", "baabbaba", "bbabaaab",
 "aabbbaab", "abbbbabb", "bbaaaaba", "bbbababa", "abbaabba",
 "bababbbb", "aabaaabb", "babbabab", "baaaabaa", "ababbaba",
 "aaabaabb", "bbaaabaa", "baaaaabb", "bbaabaab", "bbababab",
 "aabaaaab", "aaaaabab", "aabbaaba"],
"U"
Returns: "x"
7)

["q", "M", "w", "y", "p", "N", "s", "r", "a", "H", "o", "n",
 "F", "m", "l", "b", "D", "j", "C", "u", "f", "I", "g", "L",
 "i", "x", "A", "G", "O", "k", "h", "d", "c", "E", "B", "v",
 "J", "z", "K", "e", "t"],
["aabbaaabb", "baabababb", "bbaababba", "bbbaaaaaa", "abaaaabaa",
 "bababbbab", "abbaabbaa", "aabababbb", "bababaaaa", "abbababaa",
 "aabbbbbba", "bbabbabab", "babaabbba", "babbabbbb", "baaabbbbb",
 "baaabaaaa", "aaabbaaab", "abbaabbbb", "abbabbbab", "bbaaaabba",
 "babbaaabb", "aabbabbab", "baaababba", "ababaabab", "bbbaabbab",
 "aaaabbabb", "babaaaaaa", "abbbbaaab", "aabaaabba", "bbbaaaaba",
 "bbbbbbaab", "aabbaaabb", "aabaabbab", "aababaaba", "bbabbbbab",
 "abbabaaab", "babaaabbb", "bababbaaa", "aabbaabaa", "baaabbabb",
 "bbbbbbbbb"],
["m", "k", "n", "q", "L", "E", "M", "l", "w", "x", "g", "e",
 "i", "z", "F", "r", "a", "h", "f", "D", "J", "K", "j", "v",
 "A", "t", "N", "y", "s", "c", "o", "p", "d", "b", "B", "G",
 "O", "I", "u", "C", "H"],
["bbaaabbba", "bbaaaaaab", "abaaababb", "baaaabbbb", "abbbababa",
 "baaaaaaaa", "aabbbbbab", "aaaaabbba", "baabababb", "babaaabab",
 "baaababaa", "bbbbaabba", "bbaabbabb", "bbaaababb", "abbabbaba",
 "aababaaab", "abbbbbbaa", "aabbaabaa", "bbbaabbba", "abbabbaba",
 "aaabbbaaa", "bbaabaaaa", "aabababbb", "abbbbabab", "baaabbbba",
 "bababbbba", "aababbaab", "bbaabbaab", "bbbaaabbb", "babbbbabb",
 "ababababb", "babaaabab", "bbaaaaaba", "aaaaabaaa", "abbaaabbb",
 "bbbbababb", "baabababb", "bbaabaaaa", "aaababbbb", "abbbbbbba",
 "bbaabbaaa"],
"o"
Returns: "C"

Status: Functionally Complete
Todo: Use PriorityQueue for better average runtime, cleanup tests
"""

class MatchMaking(object):
    def __init__(self):
        pass

    @staticmethod
    def makeMatch(namesWomen, answersWomen, namesMen, answersMen, queryWoman):
        """ (string) Matches men and women according to their equivalent answer count,
            with ties broken via lexocographic precedence. Returns queryWoman match"""

        def getAnswerScore(w_answers, m_answers):
            """ (int) Does string comparison of answers, returns scores of matches """

            score = 0
            for i in range(len(w_answers)):
                if w_answers[i] == m_answers[i]:
                    score += 1

            return score

        # Zip together the names and respective answers, then lexo sort
        womenAnswers = sorted(zip(namesWomen, answersWomen))
        menAnswers = sorted(zip(namesMen, answersMen))

        matches = dict()

        # This is o(m*n), which isn't stellar.  This should actually use
        #  a PriorityQueue for an improved average runtime.
        for woman in womenAnswers:
            answerScore = 0
            topScore = 0
            for man in menAnswers:
                if man[0] not in matches.values():
                    answerScore = getAnswerScore(woman[1], man[1])
                    if (answerScore > topScore) or (topScore == 0):
                        topScore = answerScore
                        bestMatch = man
                else:
                    continue
            matches[woman[0]] = bestMatch[0]

        return matches[queryWoman]

def main():
    """ sup main """
    
    tests = [(["Constance", "Bertha", "Alice"],
["aaba", "baab", "aaaa"],
["Chip", "Biff", "Abe"],
["bbaa", "baaa", "aaab"],
"Bertha"),
             (["Constance", "Bertha", "Alice"],
["aaba", "baab", "aaaa"],
["Chip", "Biff", "Abe"],
["bbaa", "baaa", "aaab"],
"Constance"),
             (
["Constance", "Alice", "Bertha", "Delilah", "Emily"],
["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
["Ed", "Duff", "Chip", "Abe", "Biff"],
["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
"Constance"),
             (["Constance", "Alice", "Bertha", "Delilah", "Emily"],
["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
["Ed", "Duff", "Chip", "Abe", "Biff"],
["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
"Delilah"),
            (["Constance", "Alice", "Bertha", "Delilah", "Emily"],
["baabaa", "ababab", "aaabbb", "bababa", "baabba"],
["Ed", "Duff", "Chip", "Abe", "Biff"],
["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"],
"Emily"),
            (["anne", "Zoe"],
["a", "a"],
["bob", "chuck"],
["a", "a"],
"Zoe"),
            (["F", "M", "S", "h", "q", "g", "r", "N", "U", "x", "H", "P",
 "o", "E", "R", "z", "L", "m", "e", "u", "K", "A", "w", "Q",
 "O", "v", "j", "a", "t", "p", "C", "G", "k", "c", "V", "B",
 "D", "s", "n", "i", "f", "T", "I", "l", "d", "J", "y", "b"],
["abaabbbb", "bbaabbbb", "aaabaaab", "aabbaaaa", "baabbaab",
 "aaababba", "bbabbbbb", "bbbabbba", "aaabbbba", "aabbbaaa",
 "abbabaaa", "babbabbb", "aaaaabba", "aaaabbaa", "abbbabaa",
 "babababa", "abbaaaaa", "bbababba", "baaaaaba", "baaaaabb",
 "bbbbabba", "ababbaaa", "abbbabab", "baabbbaa", "bbbaabbb",
 "aababbab", "ababbabb", "abbaabba", "baabbabb", "aaabaaab",
 "aabbbaba", "aabaaabb", "abababba", "aabbaaaa", "aabbabaa",
 "bababaaa", "aabaaaab", "bbbbaabb", "baaababb", "abaabbab",
 "aabbbaaa", "baabbaba", "bbabbbaa", "aabbbbaa", "abbbaaab",
 "abababbb", "ababaaba", "bababaaa"],
["f", "C", "v", "g", "Q", "z", "n", "c", "B", "o", "M", "F",
 "u", "x", "I", "T", "K", "L", "E", "U", "w", "A", "d", "t",
 "e", "R", "D", "s", "p", "q", "m", "r", "H", "j", "J", "V",
 "l", "a", "k", "h", "G", "y", "i", "P", "O", "N", "b", "S"],
["bbbaabab", "bbabaabb", "ababbbbb", "bbbababb", "baababaa",
 "bbaaabab", "abbabbaa", "bbbabbbb", "aabbabab", "abbababa",
 "aababbbb", "bababaab", "aaababbb", "baabbaba", "abaaaaab",
 "bbaababa", "babaabab", "abbabbba", "ababbbab", "baabbbab",
 "babbaaab", "abbbbaba", "bbabbbba", "baaabaab", "ababbabb",
 "abbbaabb", "bbbbaabb", "bbbaaabb", "baabbaba", "bbabaaab",
 "aabbbaab", "abbbbabb", "bbaaaaba", "bbbababa", "abbaabba",
 "bababbbb", "aabaaabb", "babbabab", "baaaabaa", "ababbaba",
 "aaabaabb", "bbaaabaa", "baaaaabb", "bbaabaab", "bbababab",
 "aabaaaab", "aaaaabab", "aabbaaba"],
"U"),
            (["q", "M", "w", "y", "p", "N", "s", "r", "a", "H", "o", "n",
 "F", "m", "l", "b", "D", "j", "C", "u", "f", "I", "g", "L",
 "i", "x", "A", "G", "O", "k", "h", "d", "c", "E", "B", "v",
 "J", "z", "K", "e", "t"],
["aabbaaabb", "baabababb", "bbaababba", "bbbaaaaaa", "abaaaabaa",
 "bababbbab", "abbaabbaa", "aabababbb", "bababaaaa", "abbababaa",
 "aabbbbbba", "bbabbabab", "babaabbba", "babbabbbb", "baaabbbbb",
 "baaabaaaa", "aaabbaaab", "abbaabbbb", "abbabbbab", "bbaaaabba",
 "babbaaabb", "aabbabbab", "baaababba", "ababaabab", "bbbaabbab",
 "aaaabbabb", "babaaaaaa", "abbbbaaab", "aabaaabba", "bbbaaaaba",
 "bbbbbbaab", "aabbaaabb", "aabaabbab", "aababaaba", "bbabbbbab",
 "abbabaaab", "babaaabbb", "bababbaaa", "aabbaabaa", "baaabbabb",
 "bbbbbbbbb"],
["m", "k", "n", "q", "L", "E", "M", "l", "w", "x", "g", "e",
 "i", "z", "F", "r", "a", "h", "f", "D", "J", "K", "j", "v",
 "A", "t", "N", "y", "s", "c", "o", "p", "d", "b", "B", "G",
 "O", "I", "u", "C", "H"],
["bbaaabbba", "bbaaaaaab", "abaaababb", "baaaabbbb", "abbbababa",
 "baaaaaaaa", "aabbbbbab", "aaaaabbba", "baabababb", "babaaabab",
 "baaababaa", "bbbbaabba", "bbaabbabb", "bbaaababb", "abbabbaba",
 "aababaaab", "abbbbbbaa", "aabbaabaa", "bbbaabbba", "abbabbaba",
 "aaabbbaaa", "bbaabaaaa", "aabababbb", "abbbbabab", "baaabbbba",
 "bababbbba", "aababbaab", "bbaabbaab", "bbbaaabbb", "babbbbabb",
 "ababababb", "babaaabab", "bbaaaaaba", "aaaaabaaa", "abbaaabbb",
 "bbbbababb", "baabababb", "bbaabaaaa", "aaababbbb", "abbbbbbba",
 "bbaabbaaa"],
"o")]

    for item in tests:
        print "Match for %s: %s" % (item[4], MatchMaking.makeMatch(*item))

if __name__ == "__main__":
    main()
