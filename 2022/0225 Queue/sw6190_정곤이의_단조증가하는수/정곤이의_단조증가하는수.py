import sys
sys.stdin = open("s_input.txt")

testcase = int(input())

for testcase_num in range(1, testcase + 1):
    N = int(input())

    num_lst = list(map(int, input().split()))

    ans_max = -1

    # 두 수를 곱한 모든 값을 리스트에 넣어줌
    for one in range(len(num_lst)):
        for two in range(one + 1, len(num_lst)):
            # all_by_lst.append(num_lst[one] * num_lst[two])

            # 그냥 리스트에 안넣고 바로바로 확인할게요
            ans = num_lst[one] * num_lst[two]

            out = -1

            tmp = ans % 10 # 1의 자리 수
            inp = ans // 10

            for _ in range(20): # 낮은 자리 수가 발생할 수 있는 최솟값인 0이되면 안대요
                
                ntmp = inp % 10 # 10의 자리 수

                if ntmp > tmp: # 10의 자리 수가 크면 단조증가가 아님 
                    out = -1
                    break

                tmp = ntmp
                
                inp = inp // 10

                out = ans
                if inp == 0:
                    break
            # 단조증가면 ans 그대로 나오고, 아니면 -1이 나와요


            if ans_max < out: # 큰걸 저장할게요
                ans_max = out


    print(f'#{testcase_num} {ans_max}')

