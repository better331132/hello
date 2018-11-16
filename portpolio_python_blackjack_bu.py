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
for i in range(0,2):
        if player[i][-1] in ['0','J','Q','K']:
                card_point_p = 10
        elif player[i][-1] == 'A':
                card_point_p = 11
        else :
                card_point_p = int(player[i][-1])
        sum_p += card_point_p
print("당신의 카드 목록입니다.",player)
print("현재 당신의 점수는 {}입니다.".format(sum_p))
print('')
while True:
        hit_stay = input("카드를 추가하시겠습니까? (y/n) >> ")
        if hit_stay == "y":
                player.append(new_card.pop(0))
                if player[-1][-1] in ['0','J','Q','K']:
                        card_point_p = 10
                elif player[-1][-1] == 'A':
                    if sum_p > 10 :
                            card_point_p = 1
                    else :
                            card_point_p = 11
                else :
                        card_point_p = int(player[-1][-1])
                sum_p += card_point_p
                print('')
                print("당신의 카드 목록입니다.",player)
                print("현재 당신의 점수는 {}입니다.".format(sum_p))
                if sum_p > 21 :
                        break
                continue

        if hit_stay == "n":
                print('')
                break        

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

print("딜러의 카드 목록입니다.",dealer)
print("딜러의 최종 점수입니다.",sum_d)
print('')

if sum_p > 21 :
        print("당신의 점수가 21을 초과하였습니다.\n패배입니다.")
elif sum_p <= 21 and sum_d > 21 :
        print("딜러의 점수가 21을 초과하였습니다.\n승리하셨습니다.")
else :
        if sum_p > sum_d :
                print("승리하셨습니다.")
        elif sum_p < sum_d :
                print("패배하셨습니다.")
        else :
                print("무승부입니다.")