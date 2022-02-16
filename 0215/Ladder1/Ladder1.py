import sys
sys.stdin = open("input.txt")


for quest in range(10):
    lst = []
    quest_num = int(input())


    for _ in range(100):
        one = [0] + list(map(int, input().split())) + [0]
        lst.append(one)
    # lst에 100 by 100 으로 입력받음
    # 양쪽에 0으로 된 줄 놓음 (인덱스 오류 방지)

    fin = lst[99].index(2)
    # 종점 위치 99, 57 fin = 57
    # 58
    
    ny = 99
    nx = fin
    # 위치 추적 시작할 위치 (종점 위치)

    dx = [-1, 0, 1]
    dy = [0, -1, 0]
    # 델타 위치이동. 0좌 1상 2우 이동

    while ny >= 0:
    # y 축 인덱스 값이 0보다 큰 동안 진행 ?) 같은 경우는?

        ly = ny + dy[0]
        lx = nx + dx[0]
        # 좌측 좌표

        ry = ny + dy[2]
        rx = nx + dx[2]
        # 우측 좌표

        ty = ny + dy[1]
        tx = nx + dx[1]
        # 상측 좌표

        if lst[ly][lx] == 1:
            ny = ly
            nx = lx
            for _ in range(100):
                ny = ny + dy[0]
                nx = nx + dx[0]
                if lst[ny + dy[0]][nx + dx[0]] == 0:
                    ny = ny + dy[1]
                    nx = nx + dx[1]
                    break
        # left check
        # 좌측이 1이 아닐 때까지 좌측 이동 반복
        # 좌측이 0이면 위로 이동

        elif lst[ry][rx] == 1:
            ny = ry
            nx = rx
            for _ in range(100):
                ny = ny + dy[2]
                nx = nx + dx[2]
                if lst[ny + dy[2]][nx + dx[2]] == 0:
                        ny = ny + dy[1]
                        nx = nx + dx[1]
                        break
        # right check
        # 우측이 1이 아닐 때까지 우측 이동 반복
        # 우측이 0이면 위로 이동

        else:
            ny = ty
            nx = tx
        # move up


        print(f'{quest_num} {nx - 1}')
        # 인덱스 오류 방지하려고 임의로 넣어준 0에 의한 변화 보상





