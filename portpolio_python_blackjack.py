import random
cardsort = ['Clover','Diamond','Heart','Spade']
cardnum = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
new_card = []
for i in cardsort:
    for n in cardnum:
        k = i + n
        new_card.append(k)
random.shuffle(new_card)
