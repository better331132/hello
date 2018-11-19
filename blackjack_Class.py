import random
class Card:
    card_set = []
    def __init__(self):
        self.cardsort = ['Clover','Diamond','Heart','Spade']                         
        self.cardnum = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for s in self.cardsort:
            for n in self.cardnum:
                self.card_set.append(s + n)

class Deck(Card):
    def __init__(self):
        random.shuffle(self.card_set)

card = Card()
# print(card.card_set)
shuffled_deck = Deck()
deck = shuffled_deck.card_set
print(deck)

class Dealer:
    def __init__(self):
        self.