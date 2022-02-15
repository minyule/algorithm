import sys
sys.stdin = open("sample_input(1).txt")

quest = int(input())

for quest_num in range(quest):
    N, K = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = 12
    emp_lst = []
    ans = 0
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                emp_lst.append(A[j])
        if len(emp_lst) == N:
            total = 0
            for nums in emp_lst:
                total = total + nums
            if total == K:
                ans = ans + 1
        emp_lst = []

    print(f'#{quest_num+1} {ans}')