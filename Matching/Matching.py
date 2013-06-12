"""
http://community.topcoder.com/stat?c=problem_statement&pm=2249


Problem Statement for Matching

You are playing a game in which you have to find sets of three cards that share certain characteristics. Each card has some symbols on it. Each symbol is either a circle, a squiggle, or a diamond. Each symbol is either colored blue, red, or green. Each symbol is either solid, striped, or empty. And finally each card has either one, two, or three occurrences of the same symbol. A set is formed by three cards, and each characteristic is either the same on all three cards or different on all three cards.

For example, a card with one solid blue diamond, a card with two solid green diamonds, and a card with three solid red diamonds all form a set. The symbols on each card have the same shape and the same shading, and none of the cards has the same number or the same color. Any two cards will form a set with exactly one other card. You want to know, given two cards, what is the other card that completes the set. Create a class Matching with a method findMatch that takes two String[]s, first and second, representing the characteristics of two cards, and returns a String[] representing the characteristics of the third card.

First and second will both contain exactly four elements. The first element of each will denote the shape of the symbols on the card and will be either "CIRCLE", "SQUIGGLE", or "DIAMOND". The second element will denote the color and will be either "RED", "BLUE", or "GREEN". The third element of each will denote the shading and will be either "SOLID", "STRIPED", or "EMPTY". The fourth element of each will denote the number of symbols, and will be either "ONE", "TWO", or "THREE". The return element should contain exactly four elements, and should follow the same format as the input.
 
Definition
        
Class:  Matching
Method: findMatch
Parameters: String[], String[]
Returns:    String[]
Method signature:   String[] findMatch(String[] first, String[] second)
(be sure your method is public)
    
 
Constraints
-   first and second will both contain exactly four elements.
-   The first element of first and second will be either "CIRCLE", "SQUIGGLE", or "DIAMOND".
-   The second element of first and second will be either "RED", "BLUE", or "GREEN".
-   The third element of first and second will be either "SOLID", "STRIPED", or "EMPTY".
-   The fourth element of first and second will be either "ONE", "TWO", or "THREE".
 
Examples
0)  
        
["DIAMOND", "BLUE", "SOLID", "ONE"],
["DIAMOND", "GREEN", "SOLID", "TWO"]
Returns: [ "DIAMOND",  "RED",  "SOLID",  "THREE" ]
The example from above.
1)  
        
["CIRCLE", "GREEN", "EMPTY", "TWO"],
["DIAMOND", "BLUE", "STRIPED", "ONE"]
Returns: [ "SQUIGGLE",  "RED",  "SOLID",  "THREE" ]
All four characteristics are different on these two cards, so all four characteristics will be different on the third card in the set.
2)  
        
["DIAMOND", "RED", "SOLID", "ONE"],
["SQUIGGLE", "BLUE", "SOLID", "TWO"]
Returns: [ "CIRCLE",  "GREEN",  "SOLID",  "THREE" ]
The only characteristic that is the same for all the cards in this set is that they are all solid.
3)  
        
["SQUIGGLE", "RED", "STRIPED", "ONE"],
["SQUIGGLE", "RED", "STRIPED", "ONE"]
Returns: [ "SQUIGGLE",  "RED",  "STRIPED",  "ONE" ]


Status: Complete
Runtime: O(n * m) where n == number of cards to process and m == max(len(attributes))
  ...this is assuming we ever grow the number of cards or attributes, but for this 
  specific example, it's safe to say we're running in constant time given both n 
  and m are trivially small.
"""

class Matching(object):
    def __init__(self):
        pass

    @staticmethod
    def findMatch(card1, card2):
        """ (returns list of card attributes) Given four attributes from two
            cards, return appropriate third card.  For each attribute, all 
            cards must either have the same values, or unique values.  """

        # Setup attribute sets, so we can do set ops
        shapes = set(['CIRCLE', 'SQUIGGLE', 'DIAMOND'])
        colors = set(['RED', 'BLUE', 'GREEN'])
        patterns = set(['SOLID', 'STRIPED', 'EMPTY'])
        numbers = set(['ONE', 'TWO', 'THREE'])

        # Arrange the attributes in the same order in which they are ingested
        attribs = [shapes, colors, patterns, numbers]
        new_card = list()

        for i in range(len(card1)):
            # If attribute is the same, make it the same for the third card
            if card1[i] == card2[i]:
                new_card.append(card1[i])
            # If attributes are different, find a unique value for third card
            else:
                new_card.append((attribs[i] - set([card1[i], card2[i]])).pop())

        return new_card


def main():
    """ sup main """
    
    tests = [(["DIAMOND", "BLUE", "SOLID", "ONE"],
             ["DIAMOND", "GREEN", "SOLID", "TWO"]),
             (["CIRCLE", "GREEN", "EMPTY", "TWO"],
             ["DIAMOND", "BLUE", "STRIPED", "ONE"]),
             (["DIAMOND", "RED", "SOLID", "ONE"],
             ["SQUIGGLE", "BLUE", "SOLID", "TWO"]),
             (["SQUIGGLE", "RED", "STRIPED", "ONE"],
             ["SQUIGGLE", "RED", "STRIPED", "ONE"]),]

    for test in tests:
        print Matching.findMatch(*test)

if __name__ == "__main__":
    main()



