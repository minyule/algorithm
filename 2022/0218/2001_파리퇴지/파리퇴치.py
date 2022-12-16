import sys
sys.stdin = open("input.txt")

quest = int(input())

for quest_num in range(quest):

    N, M = map(int, input().split())

    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    # lst 입력받음

    max = 0

    # 다음 행으로 이동
    for move_y in range(0, N-M+1):

        tmp = 0
        
        for x_idx in range(0, M):
            for y_idx in range(0, M):
                tmp = tmp + lst[move_y + y_idx][x_idx]
        if max < tmp:
                max = tmp
        # 처음 나온 값을 max에 저장

        # 한 행에서 옮겨가며 확인
        for move_x in range(0, N-M):

            # 이동시 빠질 맨 앞열의 합
            minus = 0
            for y_before in range(0, M):
                minus = minus + lst[move_y + y_before][move_x]

            # 이동시 더해질 다음 열의 합
            plus = 0
            for y_after in range(0, M):
                plus = plus + lst[move_y + y_after][M + move_x]

            tmp = tmp + plus - minus

            if max < tmp:
                max = tmp

    print(f'#{quest_num + 1} {max}')