import random

while True:
    card_flow = []
    class Deck:
        def __init__(self):
            self.cards = []
            self.cardsort = ['Clover','Diamond','Heart','Spade']                         
            self.cardnum = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
            for s in self.cardsort:
                for n in self.cardnum:
                    self.cards.append(s + n)

        def shuffle_cards(self):
            random.shuffle(self.cards)
        
        def pop_card(self):
            card_flow.append(self.cards.pop(0))


    class Person:
        def __init__(self):
            self.pocket =[]

        def dealt_card(self):
            self.pocket.append(card_flow.pop(0))
        
        def value_assign(self):
            self.sum_i = 0
            for i in range(len(self.pocket)):
                if self.pocket[i][-1] in ['0', 'J', 'Q', 'K']:
                    card_value = 10
                elif self.pocket[i][-1] in 'A':
                    card_value = 11
                else:
                    card_value = int(self.pocket[i][-1])
                self.sum_i = self.sum_i + card_value

        
        def havemanya(self):
            self.quant_a = 0
            for i in range(len(self.pocket)):
                if self.pocket[i][-1] == 'A':
                    exist_a = 1
                else:
                    exist_a = 0
                self.quant_a = self.quant_a + exist_a
            print("\n당신의 카드목록입니다.>> ",self.pocket,"\n")
            print("당신은 A를 {}개 보유하고 있습니다.".format(self.quant_a))
        
        def trans_a(self):
            self.final_score = 0
            if self.quant_a == 0:
                self.final_score = self.sum_i
            else:
                q = input("\n1점으로 간주할 A의 개수를 선택해주세요.({})개까지 가능 >> ".format(self.quant_a))
                self.final_score = self.sum_i - 10 * int(q)

    class Player(Person):
        def add_card(self):
            print("\n당신의 현재 점수는 {}점 입니다.\n".format(self.final_score))
            hos = input("카드를 더 받으시겠습니까?(y/n) >> ")
            self.det = 'hit'
            if hos == 'y':
                self.det = 'hit'
            else:
                self.det = 'stay'

    class Dealer(Person):
        def havemanya(self):
            self.quant_a = 0
            for i in range(len(self.pocket)):
                if self.pocket[i][-1] == 'A':
                    exist_a = 1
                else:
                    exist_a = 0
                self.quant_a = self.quant_a + exist_a   
        
        def trans_a(self):
            self.final_score = 0
            if self.sum_i >= 17:
                while self.sum_i > 21 and self.quant_a >= 1:
                    self.quant_a = self.quant_a - 1
                    self.sum_i = self.sum_i - 10
                self.final_score = self.sum_i
            else :
                self.final_score = self.sum_i
        
        def add_card(self):
            self.det ='hit'
            if self.final_score < 17:
                self.det = 'hit'
            else:
                self.det = 'stay'


    deck = Deck()
    deck.shuffle_cards()
    dealer = Dealer()
    player = Player()
    deck.pop_card()
    dealer.dealt_card()
    deck.pop_card()
    player.dealt_card()

    while True:
        deck.pop_card()
        dealer.dealt_card()
        dealer.value_assign()
        dealer.havemanya()
        dealer.trans_a()
        dealer.add_card()
        if dealer.det == 'stay':
            break

    while True:
        deck.pop_card()
        player.dealt_card()
        player.value_assign()
        player.havemanya()
        player.trans_a()
        if player.final_score > 21:
            print("21점을 초과하였습니다.\n\n당신은 패배하셨습니다.\n")
            break
        player.add_card()
        if player.det == 'stay':
            break
    
    print("당신의 카드목록입니다.>> ",player.pocket)
    print("\n당신의 최종 점수는 {}점 입니다.".format(player.final_score))
    print("\n딜러의 최종 점수는 {}점 입니다.\n".format(dealer.final_score))
    print("딜러의 카드목록입니다.>> ",dealer.pocket,"\n")
    if player.final_score > 21:
        print("당신의 점수가 21점을 초과하였습니다.\n\n당신은 패배하셨습니다.")
    elif player.final_score <= 21 and dealer.final_score > 21 :
        print("딜러의 점수가 21점을 초과하였습니다.\n\n당신은 승리하셨습니다.")
    else:
        if player.final_score > dealer.final_score:
            print("당신의 점수가 딜러의 점수보다 높습니다.\n 당신은 승리하셨습니다.")
        elif player.final_score == dealer.final_score:
            print("당신의 점수가 딜러의 점수와 같습니다.\n 무승부입니다.")
        else :
            print("당신의 점수가 딜러의 점수보다 낮습니다.\n 당신은 패배하셨습니다.")
    
    reset = input("\n게임을 더 하시겠습니까?(y/n)>> ")
    if reset == 'y':
        continue
    if reset == 'n':
        print("\n게임종료")
        break

