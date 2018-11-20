import random
def card_value(x):
    if x == 'A':
        return 11
    elif x in ['0','J','Q','K']:
        return 10
    else :
        return int(x)
card_value('A')
print(card_value('A'))
# class Card:
#     card_set = []
#     def __init__(self):
#         self.cardsort = ['Clover','Diamond','Heart','Spade']                         
#         self.cardnum = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#         for s in self.cardsort:
#             for n in self.cardnum:
#                 self.card_set.append(s + n)
    
# class Deck(Card):
#     def __init__(self):
#         random.shuffle(self.card_set)

# card = Card()
# shuffled_deck = Deck()
# deck = shuffled_deck.card_set
# # print(deck)

# class EachDeck:
#     poped_card = []
#     def card_pick(self):        
#         # print(deck)
#         self.pick = deck.pop(0)
#         print(self.pick)
#         self.poped_card.append(self.pick)
    

# # class DealerDeck(EachDeck):

# person = EachDeck()
# person.card_pick()
# print(person.pick)
# print(person.poped_card)