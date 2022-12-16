import sys
sys.stdin = open("벌꿀채취.txt")

testcase = int(input())

N, M, C = map(int, input().split()) # 벌통 크기, 선택가능 벌통 개수, 채취 가능 꿀 최대 양

map_lst = []
for _ in range(N):
    map_lst.append(list(map(int, input().split())))

# 두 일꾼은 가로로 연속된 M개의 벌통을 선택하고 꿀 채취함. 중복 x
# 하나의 벌통은 하나의 용기에 담기. 일부만 채취 불가 ( 한번에 채취)
# 채취한 꿀은 시장에서 각 용기의 꿀의 양의 제곱만큼 수익 발생
# 두 일꾼의 수익 합이 최대가 되는 경우, 최대 수익 출력 #

total_honeys = []

# 첫 번째 일꾼이 정해요
for y1 in range(N):
    for x1 in range(N -M +1):
        p1_honey_squre = 0
        p1_honey = 0
        for honey in range(M):
            # print(honey)
            nx1 = x1 + honey
            p1_honey = p1_honey + map_lst[y1][nx1]
            p1_honey_squre = p1_honey_squre + map_lst[y1][nx1] * map_lst[y1][nx1]
        
        if p1_honey <= C: # 채집 가능 꿀 양 넘지 않아야 함. 안넘으면 p2 정해줌
            print("p1", p1_honey_squre, p1_honey)
            for y2 in range(N):
                if y2 == y1: # 같은 줄인 경우
                    # x 축이 겹치지 않는 곳에 자리 잡아야함.
                    for x2 in range(N -M +1):
                        p2_honey_squre = 0
                        p2_honey = 0
                        swit = 0
                        for honey in range(M):
                            nx2 = x2 + honey
                            if nx2 in range(nx1-M+1, nx1 +1): # p1이랑 겹치면###########################
                                swit = 1
                                break
                            # if swit == 0:
                            p2_honey = p2_honey + map_lst[y2][nx2]
                            p2_honey_squre = p2_honey_squre + map_lst[y2][nx2] * map_lst[y2][nx2]

                        if swit == 0 and p2_honey <= C:
                            print("p2_honew", p2_honey)
                            total_honeys.append(p1_honey_squre + p2_honey_squre)
                    # print("p2", p2_honey_squre, p2_honey)

                else: # 다른 줄인 경우
                    for x2 in range(N -M +1):
                        p2_honey = 0
                        for honey in range(M):
                            nx2 = x2 + honey
                            p2_honey = p2_honey + map_lst[y2][nx2]
                        if p2_honey <= C:
                            total_honeys.append(p1_honey_squre + p2_honey_squre)

                            
            # 같은 줄에서 p2 정함
            # 다른 줄에서 p2 정함
        
        print(p1_honey, p1_honey_squre, p2_honey, p2_honey_squre)
print(max(total_honeys))




# print(map_lst)