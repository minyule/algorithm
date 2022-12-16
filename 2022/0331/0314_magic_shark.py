from pprint import pprint
from re import I
import sys
sys.stdin = open("input_magic_shark.txt")

# 전체는 N by N (홀수)

lst_map = [] # 지도
lst_sand = [] # 모래 양
N = int(input())
for _ in range(N):
    lst_map.append(list(map(int, input().split())))
    lst_sand.append([0] * N)

# 가운데에서 시작
nx = N // 2
ny = N // 2

# 이동하기 왼0, 아래1, 오른2, 위3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_num = 0
re = 0
dum = 1

# 모래 퇴적 5, 10, 10, 7, 7, 2, 2, 1, 1, 알파 (왼쪽 기준)
dsx = [-2, -1, -1, 0, 0, 0, 0, 1, 1]
dsy = [0, -1, 1, -1, 1, -2, 2, -1, 1]
sand = [0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01]
real_sand = 0

# for _ in range(1+4*(N//2)+1):
while (0 <= nx < N) & (0 <= ny < N):
    
    for _ in range(re // 2 + 1):
        
        nx = nx + dx[turn_num % 4]
        ny = ny + dy[turn_num % 4]
        
        if ny < 0 or nx < 0:
            break
        

        if turn_num % 4 == 0:
        # 좌로 이동 : turn_num % 4 = 0
            no_sand = lst_map[ny][nx]
            for i in range(9):
                sx = nx + dsx[i]
                sy = ny + dsy[i]
                if 0 <= sx < N and 0 <= sy < N:
                    lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * sand[i])
                    no_sand = no_sand - int(lst_map[ny][nx] * sand[i])
            lst_map[ny][nx-1] = no_sand

        # 하로 이동
        elif turn_num % 4 == 1:
            no_sand = lst_map[ny][nx]
            for i in range(9):
                sx = nx - dsy[i]
                sy = ny - dsx[i]

                if 0 <= sx < N and 0 <= sy < N:

                    lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * sand[i])
                    no_sand = no_sand - int(lst_map[ny][nx] * sand[i])
            lst_map[ny][nx-1] = no_sand

        # 우로 이동
        if turn_num % 4 == 2:
            no_sand = lst_map[ny][nx]
            for i in range(9):
                sx = nx - dsx[i]
                sy = ny - dsy[i]
                if 0 <= sx < N and 0 <= sy < N:
                    lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * sand[i])
                    no_sand = no_sand - int(lst_map[ny][nx] * sand[i])
            lst_map[ny][nx-1] = no_sand
        
        # 상로 이동
        elif turn_num % 4 == 1:
            no_sand = lst_map[ny][nx]
            for i in range(9):
                sx = nx + dsy[i]
                sy = ny + dsx[i]

                if 0 <= sx < N and 0 <= sy < N:

                    lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * sand[i])
                    no_sand = no_sand - int(lst_map[ny][nx] * sand[i])
            lst_map[ny][nx-1] = no_sand

        # if turn_num % 4 == 0:
        #     sx = nx + dx[(turn_num + 3) % 4]
        #     sy = ny + dy[(turn_num + 3) % 4]
        #     if 0 <= sx < N and 0 <= sy < N:
        #         lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * 0.07)
        #     # lst_map[sy][sx] = 1

        #     sx = nx + dx[(turn_num + 1) % 4]
        #     sy = ny + dy[(turn_num + 1) % 4]
        #     if 0 <= sx < N and 0 <= sy < N:
        #         lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * 0.07)

        #     # 10%
        #     sx = nx + dx[(turn_num + 1) % 4] + dx[turn_num % 4]
        #     sy = ny + dy[(turn_num + 1) % 4] + dy[turn_num % 4]
        #     if 0 <= sx < N and 0 <= sy < N:
        #         lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * 0.1)

        #     sx = nx + dx[(turn_num + 3) % 4] + dx[turn_num % 4]
        #     sy = ny + dy[(turn_num + 3) % 4] + dy[turn_num % 4]
        #     if 0 <= sx < N and 0 <= sy < N:
        #         lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * 0.1)

        #     # 5%
        #     sx = nx + dx[turn_num % 4] * 2
        #     sy = ny + dy[turn_num % 4] * 2
        #     if 0 <= sx < N and 0 <= sy < N:
        #         lst_map[sy][sx] = lst_map[sy][sx] + int(lst_map[ny][nx] * 0.05)

        # 10% 인 부분
        

        # 하로 이동 : turn_num % 4 = 1


        # 우로 이동 : turn_num % 4 = 2


        # 상로 이동 : turn_num % 4 = 3


    re = re + 1
    turn_num = turn_num + 1

    

    





pprint(lst_map)
