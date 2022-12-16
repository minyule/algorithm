import sys
sys.stdin = open("s_input.txt")

quest = int(input())

for quest_num in range(quest):

    N = int(input())

    A1, B1 = map(int, input().split()) # 버스노선 i = 1
    A2, B2 = map(int, input().split()) # 버스노선 i = 2

    P = int(input())

    ans = "#" + str(quest_num + 1)

    for _ in range(P):
        route_cnt = 0

        station = int(input())

        if A1 <= station <= B1:
            route_cnt = route_cnt + 1

        if A2 <= station <= B2:
            route_cnt = route_cnt + 1
        
        ans = ans + " " + str(route_cnt)
    
    print(ans)