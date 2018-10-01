# set_game

## Rules

The game of Set operates by a few simple rules. This is essentially a pattern-finding card game. There is a deck of 81 unique cards. Each card has four features, in which there are three options for each feature. The features are shape, number, color, and texture. The possible shapes are {oval, diamond, squiggle}. The possible numbers are {1, 2, 3}. The possible colors are {red, green, purple}. The possible textures are {solid, striped, empty}. For a more detailed explanation of what these definitions are, see the official Set Card Game website for instructions (https://www.setgame.com/set) 

To play, each round, 12 cards are dealt. A set consists of three cards in which for each of the four features of the cards in the set, the features are either all the same or all different between the three cards. 

## Instructions 

To play this Python version of the game, clone this github repository and within the directory, ensuring that you are using Python3, call 

'''
python set.py
'''

From there, you will see a board of cards dealt in terminal listing the variation of each feature for each card, something like this: 

'''
('purple', 'diamond', 'empty', 3)  
('red', 'oval', 'empty', 1)  
('green', 'squiggle', 'solid', 2)  
('purple', 'squiggle', 'solid', 3)  
('purple', 'oval', 'solid', 2)  
('green', 'oval', 'empty', 3)  
('purple', 'oval', 'empty', 3)  
('purple', 'diamond', 'solid', 3)  
('green', 'squiggle', 'striped', 1)  
('red', 'squiggle', 'solid', 2)  
('green', 'oval', 'solid', 3)  
('purple', 'squiggle', 'empty', 1)  
'''

Then, a player has the option to either look for sets, ask for more cards to be dealt, or quit the game. 

To input a possible set, format your response as "a b c", where a, b, c, are the indices of the cards you would like to submit in your set. For example, submitting "0 1 2" would be submitting the set: 

'''
('purple', 'diamond', 'empty', 3)  
('red', 'oval', 'empty', 1)  
('green', 'squiggle', 'solid', 2) 
'''

Then, to ask for another three cards to be added to the board to search for more sets, simply type "deal" and enter. 

To quit the game at any point, type "quit" or "q" and enter. Note that this game will never end automatically and will only end when the player decides that they are either finished or cannot find any more sets. If a set is correctly identified, the three cards in the set will be removed and replaced with new cards from the deck, but otherwise this game, like the physical card game, is very user-dependent. 

After the user has decided that they are finished playing the game, the console will print the number of sets the user was able to correctly identify, in a message like below: 

'''
Please make a move: quit
You found  10  sets!
'''



