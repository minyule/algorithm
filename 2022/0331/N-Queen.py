import sys
sys.stdin = open("N-Queen.txt")

# N을 입력받는다.
# N by N 의 체스판에 N개의 퀸을 서로 공격하지 못한 위치에 놓는 경우의 수 찾기 #

testcase = int(input())

N = int(input())

board = []
for _ in range(N):
    board.append([0 for _ in range(N)])




print(board)