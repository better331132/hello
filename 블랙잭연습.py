class Card:
   cardtotal=[]
   def __init__(self):
       self.cardsort = ['S','C','H','D']
       self.cardnum = ['2','3','4','5','6','7','8','9','F','A','J','Q','K']
       self.sort=len(self.cardsort)
       self.num=len(self.cardnum)

   def calc(self):
       for i in self.cardsort:
           for k in self.cardnum:
               self.cardtotal.append(self.cardsort[i]+self.cardnum[k])

card = Card()
card.calc()
print(card.cardtotal)