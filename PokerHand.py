"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""
    
    def classify(self):
        '''assigns label based on strongest hand
        '''
        figures = ['One Pair', 'Two Pairs', '3 of a kind', 'straight', 'flush', 'full house', '4 of a kind', 'straight flush']
        figures_bool = [self.has_pair(), self.has_two_pair(), self.has_three(), self.has_straight(), self.has_flush(), self.has_full_house(), self.has_four(), self.has_straight_flush() ]
        try:
            index = max([i for i, v in enumerate(figures_bool) if v == True])
        except ValueError:
            index = -1
        if index == -1:
            self.label = 'No hands'
        else:
            self.label = figures[index]


    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
    
    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        self.rank_hist()
        pair_counter = 0
        for val in self.ranks.values():
            if val >= 2:
                pair_counter += 1
        return pair_counter >= 2    
    
    def has_three(self):
        self.rank_hist()
        pair_counter = 0
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False 
    
    def has_four(self):
        self.rank_hist()
        pair_counter = 0
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False 
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_full_house(self):
        return self.has_two_pair() and self.has_three()
    
    
    def has_straight(self):
        self.cards = sorted(self.cards, key=lambda x: (x.rank, x.suit))

        straight_accu = 0
        # iterate through cards sorted by rank/ suit
        for i in range(len(self.cards)-1):
            if self.cards[i+1].rank == self.cards[i].rank + 1:
                straight_accu +=1
                if (straight_accu == 3)  and (self.cards[i+1].rank == 13): #ace case
                   for card in self.cards:  #is there an ace in the hand?
                       if card.rank == 1:
                           return True
                if (straight_accu >= 4):
                    return True
            else:
                straight_accu = 0
        self.cards.sort()  #put back deck in initial sort 
        return False

    def has_straight_flush(self):
        self.cards = sorted(self.cards, key=lambda x: (x.rank, x.suit))

        straight_accu = 0
        flush_flag = True
        # iterate through cards sorted by rank/ suit
        for i in range(len(self.cards)-1):
            if self.cards[i+1].rank == self.cards[i].rank + 1:
                straight_accu +=1
                if self.cards[i+1].suit != self.cards[i].suit:
                    flush_flag = False
                if (straight_accu == 3) and flush_flag and (self.cards[i+1].rank == 13): #ace case
                    missing_ace = Card(self.cards[i+1].suit, 1)
                    if missing_ace in self.cards:
                        return True
                if (straight_accu >= 4) and flush_flag:
                    return True
            else:
                straight_accu = 0
                flush_flag = True                
        self.cards.sort()  #put back deck in initial sort 
        return False

if __name__ == '__main__':
    # make a deck
    
    
    def poker_stats(n):
        dico = dict()
        for i in range(n):
            deck = Deck()
            deck.shuffle()
            for i in range(7):
                hand = PokerHand()
                deck.move_cards(hand, 7)
                hand.classify()
                dico[hand.label]=dico.get(hand.label, 0)+(1/(7*n)*100)
        print(sorted(dico.items(), key=lambda x: -x[1]))
                
    poker_stats(10000)
    
    # deal the cards and classify the hands
    '''
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print('*'*5, 'Results: ','*'*5)
        hand.classify()
        print(hand.label)
        print('')
    '''
        

