import sys
sys.stdin = open("input.txt")

quest = int(input())

for quest_num in range(1, quest+1):
    lst = []
    for _ in range(9):
        one = list(map(int, input().split()))
        lst.append(one)
        # 스도쿠판 하나 입력받음 9 by 9

        set_1to9_row = set()
        set_1to9_col = set()

    check = 0 # 총 27개 검사할거임
    base = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 가로줄 확인 1~9 정수인지, 겹치는게 없는지
    for y in range(9):
        for x in range(9):
            if 1 <= lst[y][x] <= 9:
                set_1to9_row.add(lst[y][x])
                set_1to9_col.add(lst[x][y])

        if set_1to9_row == base:
            check = check + 1
        if set_1to9_col == base:
            check = check + 1

        set_1to9_row.clear()
        set_1to9_col.clear()

    for small_one_y in range(0, 9, 3): # 작은 네모 9개에 대해서 체크.
        for small_one_x in range(0, 9, 3):
            for y in range(3):
                for x in range(3):
                    set_1to9_row.add(lst[y][x])
            if set_1to9_row == base:
                check = check + 1

    # 정답 체크
    if check == 27:
        ans = 1
    else:
        ans = 0

    print(f'#{quest_num} {ans}')


    # 세로줄 확인

    # 작은 네모 확인