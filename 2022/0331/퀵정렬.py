import sys
sys.stdin = open("퀵정렬.txt")


# 퀵정렬
def quick_sort(lst, l, r):
    if l < r:
        s = partition(lst, l, r) # 피봇 찾는 부분
        quick_sort(lst, l, s-1)
        quick_sort(lst, s + 1, r)

def partition(lst, l, r):
    x = lst[r]
    i = l -1 
    for j in range(l, r):
        if lst[j] <= x:
            i+=1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[r] = lst[r], lst[i+1]
    return i+1



testcase = int(input())
for test_num in range(1, testcase + 1):
    N = int(input())

    lst = list(map(int, input().split()))
    # print(lst)
    quick_sort(lst, 0, N-1)
    print(f"#{test_num} {lst[N//2]}")
