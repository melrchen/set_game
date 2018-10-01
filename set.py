import math
import random
import os, sys 
import numpy as np

#######CONSTANTS FOR CLEAN CODE######
#These are the possible options for each of the four features on each card
colors = ['red', 'purple', 'green']
shapes = ['oval', 'diamond', 'squiggle']
textures = ['solid', 'striped', 'empty']
numbers = [1, 2, 3]

# card_deck contains the deck of all 81 unique combinations of these colors, shapes, textures, and numbers
def new_deck(): 
    deck = []
    for c in colors: 
        for s in shapes: 
            for t in textures: 
                for n in numbers: 
                    deck.append((c, s, t, n))
    random.shuffle(deck)
    return deck

#checks that given a set of three cards that all of the features are either all same or all different
def check_set(s): 
    for i in range(4): 
        equal = (s[0][i] == s[1][i] == s[2][i])
        different = (s[0][i] != s[1][i] and s[0][i] != s[2][i] and s[1][i] != s[2][i])
        if not (equal or different): 
            return False
    return True

#prints the board of 12 cards at a time
def print_board(cards): 
    r = len(cards)//3
    for row in range(r): 
        for column in range(3): 
            print(cards[row*3+column], " ")

#adds three more cards to the board 
def deal_more(deck, cards): 
    cards.extend(deck[:3])
    deck = deck[3:]

#replaces the set of cards just removed with new cards from the deck
#c1, c2, c3 are in increasing order. 
def replace_cards(deck, cards, c1, c2, c3): 
    cards = cards[:c1] + cards[c1+1: c2] + cards[c2+1: c3]
    if len(deck) < 3: 
        cards.extend(deck)
        deck = []
    else: 
        cards.extend(deck[:3])
        deck = deck[3:]

        

#main function that allows for user interaction
def play_game(): 
    deck = new_deck()
    sets_found = 0
    curr_board = deck[:12]
    deck = deck[12:]

    while True: 
        print_board(curr_board)
        player_set = input("Please make a move: ")
        if player_set=="quit" or player_set=="q": 
            break
        if player_set=="deal": 
            deal_more(deck, curr_board)
        else: 
            s = player_set.split()
            if len(s)>3: 
                print("please only choose 3 cards")
            else: 
                for i in range(3): 
                    s[i] = int(s[i])
                s.sort()
                set = [curr_board[i] for i in s]
                if check_set(set): 
                    sets_found+=1
                    replace_cards(deck, curr_board, s[0], s[1], s[2])
                else: 
                    print("That is not a valid set, please choose again. \n")


    print("You found ", sets_found, " sets!")


if __name__ == '__main__': 
    play_game()
