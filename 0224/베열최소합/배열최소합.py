import sys
sys.stdin = open("sample_input(3).txt")

testcase = int(input())

N = int(input()) # 배열의 가로세로 길이

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))



print(lst)