"""
http://community.topcoder.com/stat?c=problem_statement&pm=4483

Problem Statement for WordCompositionGame

Three players are playing a game of word composition in which each player writes down a list of words. After the time expires the scores are calculated using the following rules. Each player gains 3 points for each unique word that only he has, 2 points for each word that is shared with exactly one other player, and 1 point for each word that is shared with both of the other players.

You will be given String[]s listA, listB and listC - the word lists of playerA, playerB and playerC respectively. Your method should return scores of playerA, playerB and playerC in the form "scoreA/scoreB/scoreC" (quotes for clarity).

 
Definition
        
Class:  WordCompositionGame
Method: score
Parameters: String[], String[], String[]
Returns:    String
Method signature:   String score(String[] listA, String[] listB, String[] listC)
(be sure your method is public)
    
 
Constraints
-   listA, listB and listC will have between 1 and 50 elements each, inclusive.
-   Each element of listA, listB and listC will contain between 1 and 20 characters, inclusive.
-   Each element of listA, listB and listC will contain only lowercase letters ('a'-'z').
-   All elements in listA will be distinct.
-   All elements in listB will be distinct.
-   All elements in listC will be distinct.
 
Examples
0)  
        
["cat", "dog", "pig", "mouse"],
["cat", "pig"],
["dog", "cat"],
Returns: "8/3/3"
1)  
        
["mouse"],
["cat", "pig"],
["dog", "cat"],
Returns: "3/5/5"
2)  
        
["dog", "mouse"],
["dog", "pig"],
["dog", "cat"],
Returns: "4/4/4"
3)  
        
["bcdbb","aaccd","dacbc","bcbda","cdedc","bbaaa","aecae"],
["bcdbb","ddacb","aaccd","adcab","edbee","aecae","bcbda"],
["dcaab","aadbe","bbaaa","ebeec","eaecb","bcbba","aecae","adcab","bcbda"],
Returns: "14/14/21"

Status: Complete
Runtime: O(n), where n is the total number of word entries. Specifically
 this will run in 2n time.
"""

class WordCompositionGame(object):
    def __init__(self):
        pass

    @staticmethod
    def score(*lists):
        """ (str()) Given lists A, B, and C: add up player scores and return
            a string for the scores in the format scoreA/scoreB/scoreC.
            Unique words earn 3 points, words shared once earn 2 points,
            and words shared with all players earn 1 point. This implementation
            could be faster if I optimized for using only 3 lists, but I wanted
            a generic solution that would support more than three lists. """

        words = dict()
        scores = dict()
        list_count = len(lists)

        # Iterate through lists, and build dictionary based upon
        #  who has answered what.
        for i, answer_list in enumerate(lists):
            for word in answer_list:
                new_set = words.get(word, set())
                new_set.add(i)
                words[word] = new_set

        # Iterate through word matches, and add up the scores for
        #  each list.  For this generic solution, I modified the score
        #  algorithm to be number of lists - number of other matches.
        for matches in words.values():
            match_count = len(matches)
            for num in matches:
                add = list_count - match_count + 1
                scores[num] = scores.get(num, 0) + add

        # Build score string, delimited by '/'s.
        score_return = '/'.join(str(x) for x in scores.values())
        return score_return


def main():
    """ sup main """
    
    tests = [(["cat", "dog", "pig", "mouse"],
            ["cat", "pig"],
            ["dog", "cat"]),
             (["mouse"],
            ["cat", "pig"],
            ["dog", "cat"]),
             (["dog", "mouse"],
            ["dog", "pig"],
            ["dog", "cat"]),
             (["bcdbb","aaccd","dacbc","bcbda","cdedc","bbaaa","aecae"],
            ["bcdbb","ddacb","aaccd","adcab","edbee","aecae","bcbda"],
            ["dcaab","aadbe","bbaaa","ebeec","eaecb","bcbba","aecae","adcab","bcbda"])]

    for test in tests:
        print "Answers: %s" % WordCompositionGame.score(*test)

if __name__ == "__main__":
    main()



