from pprint import pprint
import sys
sys.stdin = open("보급로.txt")

testcase = int(input())

N = int(input())

map_lst = []
for _ in range(N):
    map_lst.append(list(map(int, input())))

for x in range(1, N): # 맨 윗줄, 맨 왼쪽 줄에 있는 칸 바꿔줌. 시작 위치에서 해당 위치로 오는데 걸리는 시간
    map_lst[0][x] = map_lst[0][x] + map_lst[0][x-1]
    map_lst[x][0] = map_lst[x][0] + map_lst[x-1][0]

for n in range(2, N):
    for x in range(1, n):
        y = n-x
        sub = min(map_lst[y][x-1], map_lst[y-1][x])
        map_lst[y][x] = map_lst[y][x] + sub

        # print(x, y)
        
for n in range(2, N):
    for x in range(1, n):
        y = n-x
        print(x, y)
        # sub = min(map_lst[y][x-1], map_lst[y-1][x])
        # map_lst[y][x] = map_lst[y][x] + sub



pprint(map_lst)