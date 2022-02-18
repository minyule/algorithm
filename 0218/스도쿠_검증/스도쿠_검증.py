import sys
sys.stdin = open("input.txt")

quest = int(input())

lst = []
for _ in range(9):
    one = list(map(int, input().split()))
    lst.append(one)
    # 스도쿠판 하나 입력받음 9 by 9

    set_1to9 = set()

    # 가로줄 확인 1~9 정수인지, 겹치는게 없는지
    for y in range(9):
        for x in range(9):
            if 1 <= lst[y][x] <= 9:
                set_1to9.add(lst[y][x])
            else:
                break

        if len(set_1to9) != 9:
            break
            
            lst[y][x]

    # 세로줄 확인

    # 작은 네모 확인