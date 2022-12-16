import sys
sys.stdin = open("sample_input.txt")

quest = int(input())

for quest_num in range(quest):

    N, Q = map(int, input().split())

    ans_lst = [0] * N

    lst = []

    ans = "#" + str(quest_num + 1)

    # input
    for _ in range(Q):

        lst.append(list(map(int, input().split())))

    for lr_lst in range(len(lst)): # 입력받은 l, r을 뒤에서부터 순서대로 가져옴
        # print(lst[-lr_lst-1]) 

        for i in range(lst[-lr_lst-1][0], lst[-lr_lst-1][1] + 1):
            # l이랑 r 사이 값을 가져옴
            # print(i)

            # ans_lst에서 값이 0이면
            if ans_lst[i-1] == 0:
                ans_lst[i-1] = Q
            
        Q = Q-1

    for i in ans_lst:
        ans = ans + " " + str(i)

    print(ans)

