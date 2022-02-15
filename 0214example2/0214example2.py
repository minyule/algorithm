import sys
sys.stdin = open("input.txt")

quest = int(input())

for quest_num in range(quest):
    lst = list(map(int, input().split()))

    n = len(lst)
    total = 0
    for i in range(1<<n): # 2 ^(원소의 개수) 만큼 반복
        tmp = 0
        for j in range(n): 
            if i & (1<<j): # i의 j번 비트가 1인 경우
                tmp = lst[j] + tmp
                if tmp == 0:
                    total = 1

    print(f'#{quest_num + 1} {total}')