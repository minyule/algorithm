import sys
sys.stdin = open("input.txt")

quest = int(input())

for quest_num in range(quest):
    carrot = int(input())

    lst = list(map(int, input().split())) + [0] # 리스트 에러 방지

    max = 1 # 연속하는 숫자 개수의 최댓값. 발생할 수 있는 최소의 최댓값은 1 
    cnt = 1 # 일회용으로 사용하는 연속하는 숫자의 개수. 이 역시 최소값은 1
    for now_idx in range(carrot):
        

        if lst[now_idx + 1] == lst[now_idx] + 1:
            cnt = cnt + 1 # 다음에 위치한 값이 현재 위치한 값 +1 이면 숫자 개수 하나 더함
        else: # 아니면 max값과 비교해서 큰 값을 저장하고 cnt 초기화
            if max < cnt:
                max = cnt
                cnt = 1

    print(f'#{quest_num + 1} {max}')