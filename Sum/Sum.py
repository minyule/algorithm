import sys
sys.stdin = open("input.txt")

for _ in range(10):
    quest_num = int(input())
    lst = []
    for _ in range(100):
        one_lst = list(map(int, input().split()))
        lst.append(one_lst)
    # print(quest_num, lst)
    tmp_col = 0
    tmp_row = 0
    tmp_cross = 0
    tmp_r_cross = 0
    max = lst[0][0]
    # lst[i][j] 꼴
    for j in range(100):
        tmp_col = 0
        tmp_row = 0
        
        tmp_cross = tmp_cross + lst[j][j] # 하향 대각선 합
        tmp_r_cross = tmp_r_cross + lst[-j-1][j] # 상향 대각선 합
        for i in range(100):
            tmp_col = tmp_col + lst[i][j] # 한 열의 합
            tmp_row = tmp_row + lst[j][i] # 한 행의 합

        if tmp_col > max:
            max = tmp_col
        if tmp_row > max:
            max = tmp_row
        if tmp_cross > max:
            max = tmp_cross
        if tmp_r_cross > max:
            max = tmp_r_cross
    print(f'#{quest_num} {max}')



