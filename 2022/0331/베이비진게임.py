import sys
sys.stdin = open("베이비진게임.txt")

testcase = int(input())


for test_num in range(1, testcase + 1):

    inp_lst = list(map(int, input().split()))

    p1 = [0 for _ in range(14)]
    p2 = [0 for _ in range(14)]

    for inp in range(0, 12, 2):
        p1_idx = inp_lst[inp] + 2
        p2_idx = inp_lst[inp + 1] + 2
        p1[p1_idx] += 1
        p2[p2_idx] += 1

        # print(p1, p2)
        
        # triplet 또는 run이 되면 중단 현재가 가운데가 되는 경우, 맨 왼쪽이 되는 경우, 맨 오른쪽이 되는 경우
        # p1이 이김
        if p1[p1_idx] >= 3 or (p1[p1_idx - 1] > 0 and p1[p1_idx + 1] > 0) or (p1[p1_idx + 2] > 0 and p1[p1_idx + 1] > 0) or (p1[p1_idx - 1] > 0 and p1[p1_idx - 2] > 0):
            ans = 1
            break
        # p2가 이김
        elif p2[p2_idx] >= 3 or (p2[p2_idx - 1] > 0 and p2[p2_idx + 1] > 0) or (p2[p2_idx + 2] > 0 and p2[p2_idx + 1] > 0) or (p2[p2_idx - 1] > 0 and p2[p2_idx - 2] > 0): # p2만 끝나면
            ans = 2
            break

        else: # 마지막까지 끝나지 않음
            ans = 0
        
    # print(p1, p2) 
    print(f'#{test_num} {ans}')






                # if p2[p2_idx] >= 3 or (p2[p2_idx - 1] > 0 and p2[p2_idx + 1] > 0) or (p2[p2_idx + 2] > 0 and p2[p2_idx + 1] > 0) or (p2[p2_idx - 1] > 0 and p2[p2_idx - 2] > 0): # 동시에 끝나면
            #     ans = 0
            #     break
            # else: # p1만 끝나면