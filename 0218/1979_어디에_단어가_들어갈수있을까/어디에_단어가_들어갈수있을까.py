import sys
sys.stdin = open("input.txt")

quest = int(input())

for quest_num in range(quest):

    N, K = map(int, input().split())
    # N은 전체 큰 정사각형의 한 변 길이
    # K는 넣고싶은 단어의 길이

    lst_empty_len = [0] * (N + 1)
    # 빈칸 길이별로 개수를 넣을 리스트
    # 인덱스가 빈칸의 길이를 뜻하게 됨
    # 빈칸 길이의 최대값은 N이 될것
    # 인덱스 0, 1은 사용하지 않게 될 것임 신경 쓰지 않기

    lst_all = []
    for _ in range(N):
        lst_all.append(list(map(int, input().split())) + [0])
    lst_all.append([0] * (N + 1))
    # 인덱스 에러 방지하려고 우측 하단 맨 끝에 0으로 된 행,열을 추가함




    # 1. 가로로 먼저 봐요
    for y_idx in range(N):
        tmp_len_row_moving = 1
        tmp_len_col_moving = 1

        for x_idx in range(N):
            if lst_all[y_idx][x_idx] == 1:
                if lst_all[y_idx][x_idx + 1] == 1:
                    tmp_len_row_moving = tmp_len_row_moving + 1
                else: # 다음 숫자가 0이라면 길이 리스트에 횟수 추가, tmp초기화
                    lst_empty_len[tmp_len_row_moving] = lst_empty_len[tmp_len_row_moving] + 1
                    tmp_len_row_moving = 1

            # 2. 동시에 세로로도 보려고 위에서 변수만 바꿔줘요 
            if lst_all[x_idx][y_idx] == 1:
                if lst_all[x_idx + 1][y_idx] == 1:
                    tmp_len_col_moving = tmp_len_col_moving + 1
                else: 
                    lst_empty_len[tmp_len_col_moving] = lst_empty_len[tmp_len_col_moving] + 1
                    tmp_len_col_moving = 1

    print(f'#{quest_num + 1} {lst_empty_len[K]}')



        # 빈칸 길이가 인덱스인 곳 숫자를 1 늘려줌

        # 2. 동시에 세로로도 보려고 위에서 변수만 바꿔줘요 
        # tmp_len_col_moving = 1
        # for x_idx in range(N):
        #     if lst_all[x_idx][y_idx] == 1:
        #         if lst_all[x_idx + 1][y_idx] == 1:
        #             tmp_len_col_moving = tmp_len_col_moving + 1
        #         else: 
        #             lst_empty_len[tmp_len_col_moving] = lst_empty_len[tmp_len_col_moving] + 1
        #             tmp_len_col_moving = 1