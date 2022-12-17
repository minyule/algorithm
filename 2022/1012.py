import sys
from pprint import pprint

sys.stdin = open("1012.txt")

tc = int(input())

w, h, b = map(int, input().split())
lst = [[0] * w for _ in range(h)]
lst_vst = [[0] * w for _ in range(h)]  # 배추 확인했으면 1로 바꿔줄거임

for _ in range(b):
    x, y = map(int, input().split())
    lst[y][x] = 1

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
ans = 0
for y in range(h):
    for x in range(w):
        if lst[y][x] == 1:
            if lst_vst[y][x] == 0:
                ans += 1
                # 현 위치에서 탐색 시작
                stack = [[y, x]]
                while len(stack) > 0:
                    for i in range(4):


            lst_vst[y][x] = 1  # 방문했음을 표시


pprint(lst)

