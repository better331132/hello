class Card :
    def card_set(self) :
        ['s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','sa','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ca','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk','da','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','ha']

class Deck(Card) :
    def dealt_card(self) :
        return self.pop(1)
