import sys
sys.stdin = open("컨테이너운반.txt")

# 트럭
# #

testcase = int(input())

for test_num in range(1, testcase + 1):

    N, M = map(int, input().split()) # N: 컨테이너 수, M: 트럭 수

    weights_inp = list(map(int, input().split())) # 화물 무게 리스트
    trucks_inp = list(map(int, input().split())) # 트럭 적재 용량. 항목은 M

    weights = [0 for _ in range(51)]
    trucks = [0 for _ in range(51)]

    # 해당 값 갖는 인덱스에 개수 추가해줌
    for weight in weights_inp:
        weights[weight] += 1
    for truck in trucks_inp:
        trucks[truck] += 1

    ans = 0
    for truck_idx in range(50, 0, -1): # 트럭 리스트 뒤에서부터 확인
        if trucks[truck_idx] > 0: # 사용 가능한 트럭이 있음
            for weight_idx in range(truck_idx, 0, -1): # 그 트럭적재용량부터 화물 무게 리스트를 뒤에서부터 확인
                if weights[weight_idx] > 0: # 적재할 화물이 있음
                    # 사용가능한 트럭이 없게 되면 중지
                    while trucks[truck_idx] > 0 and weights[weight_idx] > 0:
                        ans = ans + weight_idx
                        trucks[truck_idx] -= 1
                        weights[weight_idx] -= 1
                    
    print(f"#{test_num} {ans}")




