import sys
sys.stdin = open("최소생산비용.txt")

# 순열 구하기
def make_perm(perm):
    if len(perm) == r: # 길이가 되면 중지
        ord_lst.append(perm[:])
        return
    for i in lst:
        if i not in perm: # 리스트에 없으면
            perm.append(i) # 넣은 상태에서 다시 순열과정
            make_perm(perm)
            perm.pop() # 빼버림.

# 모든 가능한 순서에 대해 시행

testcase = int(input())

for test_num in range(1, testcase + 1):

    N = int(input())

    product_lst = []
    for _ in range(N):
        product_lst.append(list(map(int, input().split())))

    lst = [i for i in range(N)]
    r = N

    ord_lst = [] # 순서를 모아놓은 리스트
    make_perm([])

    min = 1e9
    for order in ord_lst: # 순서 ex) [0, 1, 2]
        sum = 0
        y = 0
        for ord in order:
            sum = sum + product_lst[y][ord]
            y = y + 1
        if min > sum:
            min = sum
    print(f"#{test_num} {min}")