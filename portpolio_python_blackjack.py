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
sum_d = 0
while True:
        dealer.append(new_card.pop(0))
        if dealer[-1][-1] in ['0','J','Q','K']:
                card_point_d = 10
        elif dealer[-1][-1] == 'A':
                if sum_d > 10 :
                        card_point_d = 1
                else :
                        card_point_d = 11
        else :
                card_point_d = int(dealer[-1][-1])
        sum_d += card_point_d
        if sum_d >= 17:
                break

print(dealer)
if sum_d > 21 :
        print(sum_d,"Burst")
elif sum_d == 21 :
        print(sum_d, "Black jack")
else :
        print(sum_d)


# print(new_card)
# print(player)

# print("플레이어 점수합 >> ", sum_p)
