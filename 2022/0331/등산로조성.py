from pprint import pprint
import sys
sys.stdin = open("등산로조성.txt")

testcase = int(input())

# 가장 높은 봉우리에서 시작
# 높은지형에서 낮은지형으로, 가로 또는 세로 방향으로
# -> 높이가 같은 곳 또는 낮은 곳 또는 대각선 불가능
# 긴 등산로를 만들기 위해 딱 한 곳을 정해서 K만큼 깎을 수 있음
# 이때 만들수있는 최대 등산로 길이 출력

N, K = map(int, input().split())

highest_val = 0 # 최고 값
map_lst = []
for _ in range(N):
    one_line = list(map(int, input().split()))
    map_lst.append(one_line)
    for one in one_line:
        if highest_val < one:
            highest_val = one

highest = [] # 최고 위치값 모아놓음
for x in range(N):
    for y in range(N):
        if map_lst[y][x] == highest_val:
            highest.append([x, y])


# 이동(상 우 하 좌)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 1. 가장 높은 봉우리에서 시작하기
now_idx = [0, 0]










pprint(map_lst)
pprint(highest)