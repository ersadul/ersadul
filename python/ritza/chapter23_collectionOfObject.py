# Chapter 23: Collections of objects
# Spades --> 3
# Hearts --> 2
# Diamonds --> 1
# Clubs --> 0
# Jack --> 11
# Queen --> 12
# King --> 13
class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank]+ ' of '+ self.suits[self.suit])
    
    # 23.4. Comparing cards
    def cmp(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # exercise 1. 
        # aces higher than the other
        if self.rank == 1: return 1
        # if suit the same, check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # if Ranks are the same, it's a tie
        return 0
    
    def __eq__(self, other):
        return self.cmp(other) == 0
    
    def __le__(self, other):
        return self.cmp(other) <= 0
    
    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0
    
    def __ne__(self, other):
        return self.cmp(other) != 0

# # check object output when we print them
# three_of_clubs = Card(0, 3)
# card1 = Card(1, 11)
# card2 = Card(1, 3)
# print(card1)
# print(card2)
# # check operation between object
# card1 = Card(1, 11)
# card2 = Card(1, 3)
# card3 = Card(1, 11)
# print(card1 < card2)
# print(card1 == card3)

# 23.5. Decks
class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # 23.6. Printing the deck
    def print_deck(self):
        for card in self.cards:
            print(card)
    
    def __str__(self):
        s = ''
        for i in range(len(self.cards)):
            s = s + ' ' * i + str(self.cards[i]) + '\n'
        return s
    
    # 23.7. Shuffling the deck
    # def shuffle(self):
    #     import random
    #     rng = random.Random()
    #     num_cards = len(self.cards)
    #     for i in range(num_cards):
    #         j = rng.randrange(i, num_cards)
    #         (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])

    # we can use shuffle method from Random
    def shuffle(self):
        import random
        rng = random.Random()   # make random object
        rng.shuffle(self.cards) # use its shuffle method

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []
    
    
# red_deck = Deck()
# blue_deck = Deck()
# # red_deck.print_deck()
# print(red_deck)


# 1. Modify cmp so that Aces are ranked higher than Kings
# test Exercise 1.
ace = Card(0, 1)
king = Card(0, 13)
print(Card.ranks[1])
print(ace.rank)
print(king.rank)
print(ace > king)