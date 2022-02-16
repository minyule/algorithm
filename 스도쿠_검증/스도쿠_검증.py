import sys
sys.stdin = open("input.txt")

quest = int(input())

lst = []
for _ in range(9):
    one = list(map(int, input().split()))
    lst.append(one)
    # 스도쿠판 하나 입력받음 9 by 9

    