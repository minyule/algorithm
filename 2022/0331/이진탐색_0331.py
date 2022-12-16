import sys
sys.stdin = open("이진탐색_0331.txt")

def find(left_idx, right_idx, target):
    global status
    global res
    # print(left_idx, right_idx, target)

    left = lstA[left_idx]
    right = lstA[right_idx]

    middle_idx = (left_idx + right_idx) // 2
    middle = lstA[middle_idx]

    # print("tar", target)
    # print("l, m, r" ,left, middle, right)

    if middle == target: # 중간 값이 찾는 값이면 리턴
        target = target
        # print("target", target)
        res = True
        # return res
    
    elif target < middle and status != 0: # 찾는 값이 왼쪽에 있으면
        right_idx = middle_idx -1
        status = 0
        # print("left")
        find(left_idx, right_idx, target)
        # return res

    elif middle < target and status != 1: # 찾는 값이 오른쪽에 있으면
        left_idx = middle_idx +1
        status = 1
        # print("right")
        find(left_idx, right_idx, target)
        # return res
    
    
    else: # 다시 같은 방향 보게 되는 경우일 듯
        # print("status", status)
        res = False
        # return res
    # return True
    return res

testcase = int(input())
for test_num in range(1, testcase + 1):

    A, B = map(int, input().split())

    lstA = list(map(int, input().split()))
    lstB = list(map(int, input().split()))
    lstA = sorted(lstA)
    # print(lstA)

    ans = 0
    # ans_lst = []

    for check in lstB:
        status = 2
        res = False
        if find(0, A-1, check):
            ans += 1
            # ans_lst.append(check)

    print(f"#{test_num} {ans}")
    # print("-------------------------")

    # sorted 안해서 테스트 케이스 몇 문제를 계속 틀렸었다