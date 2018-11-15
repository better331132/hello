import random
cardsort = ['Clover','Diamond','Heart','Spade']                         
cardnum = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

new_card = []
for i in cardsort:
    for n in cardnum:
        k = i + n
        new_card.append(k)                                              

random.shuffle(new_card)                                                


player = []                                                             
dealer = []                                                            

for i in range(0,2):
        player.append(new_card.pop(0))
        dealer.append(new_card.pop(0))

sum_p = 0
sum_d = 0
for i in range(0,2):
        if player[i][-1] in ['0','J','Q','K']:
                card_point_p = 10
        elif player[i][-1] == 'A':
                card_point_p = 11
        else :
                card_point_p = int(player[i][-1])
        sum_p += card_point_p
for i in range(0,2):
        if dealer[i][-1] in ['0','J','Q','K']:
                card_point_d = 10
        elif dealer[i][-1] == 'A':
                card_point_d = 11
        else :
                card_point_d = int(dealer[i][-1])
        sum_d += card_point_d
print(new_card)
# while card_point_d < 17:
#         dealer.append(new_card.pop(0))
#         sum_d += card_point_d
#         if card_point_d >= 17:
#                 break

# print(player)
# print(dealer)
# print("플레이어 점수합 >> ", sum_p)
# print("딜러 점수합 >> ", sum_d)