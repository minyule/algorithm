import sys
sys.stdin = open("원자소멸시뮬레이션.txt")

testcase = int(input())

atom_cnt = int(input())

# 원자의 x, y좌표, 이동방향, 보유 에너지
atom_lst = []
