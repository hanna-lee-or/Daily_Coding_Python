#라인 코딩 테스트 5번


def solution(cards):

    # 카드 4장 분배 (딜러 오픈 카드 1)
    # 플레이어 카드 더 받으실?
    # 카드 2장의 합이 21이면 그냥 바로 딜러와 승패 ㄱㄱ
    # 받는 경우
    # 카드 2장의 합이 21이하면 받을 수 있음
    # 모든 카드 합이 21이상이면 즉시 게임에서 짐

    # 받지 않는 경우
    # 뒤집은 카드 오픈, 모든 합이 17이상일 때까지 카드 추가
    # 이 때 21 넘으면 짐

    # 21에 가까운 사람이 이기며, 합이 서로 같으면 비긴다.
    # j 11, q 12, k 13
    # 이 부분은 구현 못함 ^^ => a 1 또는 11 (유리한 쪽으로)

    player_card = 0
    npc_card = 0
    player_gold = 0
    cardLength = len(cards)

    def checkI(i):
        if (i >= cardLength):
            return False
        else:
            return True

    def checkWin(npc, player):
        if (npc < player):
            return 2
        elif (npc > player):
            return -2
        else:
            return 0

    i = 0
    while i < len(cards):

        # 카드 초기 세팅
        player_card += cards[i]
        i += 1
        if (checkI(i) == False):
            return player_gold
        npc_card += cards[i]
        i += 1
        if (checkI(i) == False):
            return player_gold
        player_card += cards[i]
        i += 1
        if (checkI(i) == False):
            return player_gold
        npc_card += cards[i] # 오픈된 카드
        open_card = cards[i]
        i += 1
        if (checkI(i) == False):
            return player_gold
        
        # 카드 추가 분배 및 승패 결정
        if(player_card == 21):
            if(npc_card != 21):
                player_gold += 3
        elif(player_card > 21):
            player_gold -= 2
        else:
            flag = False
            # 플레이어가 카드를 추가로 받는 경우
            if(open_card == 1 or open_card >= 7):
                while player_card < 17:
                    player_card += cards[i]
                    i += 1
                    if (checkI(i) == False):
                        return player_gold
                    if(player_card > 21):
                        player_gold -= 2
                        flag = True
            elif(open_card == 2 or open_card == 3):
                while player_card < 12:
                    player_card += cards[i]
                    i += 1
                    if (checkI(i) == False):
                        return player_gold
                    if (player_card > 21):
                        player_gold -= 2
                        flag = True
                        
            # 플레이어 카드 추가가 21을 넘지 않은 경우
            if (flag == False):
                flag_npc = False
                while npc_card < 17 and checkI(i) == True:
                    npc_card += cards[i]
                    i += 1
                    if (npc_card > 21):
                        player_gold += 2
                        flag_npc = True
                #print(npc_card, player_card, flag_npc)
                if(flag_npc == False):
                    player_gold += checkWin(npc_card, player_card)

            #print("소지금액 :", player_gold)


    return player_gold



print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) # -2


