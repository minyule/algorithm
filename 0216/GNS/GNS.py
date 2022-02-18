import sys
sys.stdin = open("GNS_test_input.txt")

quest = int(input())

for nnn in range(quest):

    q = list(input().split())
    repeat = int(q[1])

    lst = list(input().split())
    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num_cnt = [0] * 10 # 숫자 개수 저장
    for i in range(repeat):
        for j in range(10):
            if lst[i] == nums[j]:
                num_cnt[j] = num_cnt[j] + 1

    ans = ''
    for j in range(10):
        for k in range(num_cnt[j]):
            ans = ans + nums[j] + ' '
    
    # ans = ans.rstrip()
    print(f'#{nnn + 1}')
    print(ans)

    # print(num_cnt)




    # if lst[i] == "ZRO": #0
    #     num_cnt[0] = num_cnt[0] + 1
    # elif lst[i] == "ONE":
    #     num_cnt[1] = num_cnt[1] + 1
    # elif lst[i] == "TWO":
    #     num_cnt[2] = num_cnt[2] + 1
    # elif lst[i] == "THR":
    #     num_cnt[3] = num_cnt[3] + 1
    # elif lst[i] == "FOR":
    #     num_cnt[4] = num_cnt[4] + 1
    # elif lst[i] == "FIV":
    #     num_cnt[5] = num_cnt[5] + 1
    # elif lst[i] == "SIX":
    #     num_cnt[6] = num_cnt[6] + 1
    # elif lst[i] == "SVN":
    #     num_cnt[7] = num_cnt[7] + 1
    # elif lst[i] == "EGT":
    #     num_cnt[8] = num_cnt[8] + 1
    # elif lst[i] == "NIN":
    #     num_cnt[9] = num_cnt[9] + 1

