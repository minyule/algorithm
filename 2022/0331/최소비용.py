from copy import deepcopy
from pprint import pprint
import sys
sys.stdin = open("최소비용.txt")

testcase = int(input())

# 출발은 좌상 끝, 도착은 우하 끝
# 소비 연료가 최소인 최적의 경로로 이동.
# 이동시 기본적인 연료 소비량이 1. 높이에 따른 추가 연료 소비량 있음#

# 위치이동 좌표. 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(nx, ny):
    now_distance = distance_lst[ny][nx]
    for i in range(4):
        nextX = nx + dx[i]
        nextY = ny + dy[i]
        
        if 0 <= nextX < N and 0 <= nextY < N: # 인덱스 오류 방지
            distance = abs(map_lst[ny][nx] - map_lst[nextY][nextX]) + 1 + now_distance
            if distance < distance_lst[nextY][nextX]:
                distance_lst[nextY][nextX] = distance 
    # print(nx, ny, distance_lst)
    # pprint(distance_lst)
for test_num in range(1, testcase + 1):
    N = int(input())

    map_lst = []
    
    for _ in range(N):
        map_lst.append(list(map(int, input().split())))

    distance_lst = [[10000 for _ in range(N)] for _ in range(N)]
    distance_lst[0][0] = 0



    for k in range(N**2):
        tmp_lst = distance_lst[:]
        for x in range(N):
            for y in range(N):
                check(x, y)
        print(tmp_lst, distance_lst)
        if tmp_lst == distance_lst:
            print(k)
            break
        # pprint(distance_lst)
    print(f"#{test_num} {distance_lst[N-1][N-1]}")