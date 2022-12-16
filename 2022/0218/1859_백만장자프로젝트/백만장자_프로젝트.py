import sys
sys.stdin = open("input.txt")

quest = int(input()) +1



for quest_num in range(1, quest):

    days = int(input())

    price = list(map(int, input().split()))

    # buy_price = 0 # 살 때 든 돈
    # buy_cnt = 0 # 산 물건 수

    now_idx = 0 # 앞에꺼 몽땅 사려할때 시작점

    gain = 0 # 이득

    # 가격 최대인 날짜랑 그 곳의 인덱스 찾기
    max_price = price[-1]
    max_idx = 0



    for one_price in range(-1, -len(price)-1, -1):

        if max_price > price[one_price]:
            gain = gain + (max_price - price[one_price])
        else:
            max_price = price[one_price]
        
    print(f'#{quest_num} {gain}')

















    # while now_idx < len(price)-1:

    #     for date in range(now_idx, len(price)):
    #         maxprice_tmp = price[date]
    #         if maxprice_tmp > max_price:
    #             max_price = maxprice_tmp
    #             max_idx = date


        
        
    #     # 최대인 곳 이전까지 모든 물건 사고 팔기
    #     for buying in range(now_idx, max_idx):
    #         gain = gain + (max_price - price[buying])


    #     now_idx = max_idx + 1 # 이제 최댓값 다음부터 볼거임
    #     max_price = 0

        
    # print(f'#{quest_num} {gain}')
        # print(gain)

    












# for date in range(len(price)): # 날짜에 대해 루프 돌림
    # ##### 인덱스 에러 조심! 리스트 맨 뒤에 뭐 처리해주기

    # if price[date] <= price[date + 1]: # 다음날이 더 비싸거나 같으면 사둠
    #     buy_cnt = buy_cnt + 1
    #     buy_price = buy_price + price[date]

    # # 다음 날이 더 싼경우
    # # 1. 더 뒤에 날에 비싼게 있으면 사야해
    # # 2. 더이상 비싼날이 없으면 사면 안돼. 있는거 다 팔아야해
    # else:
    #     later_max = price[date + 1] # 일단 다음날 가격 넣어놓음
    #     for later in range(date, len(price)):
    #         tmp = price[later]
    #         if tmp > later_max:
    #             later_max = tmp # 남은 날 중 최대 값을 저장해놓음
        
    #     if 