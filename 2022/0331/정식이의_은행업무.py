import sys
sys.stdin = open("정식이의_은행업무.txt")

testcase = int(input())
for test_num in range(1, testcase + 1):
    twos = input()
    threes = input()

    twos_len = len(twos)
    threes_len = len(threes)

    twos_lst = []
    threes_lst = []

    for idx in range(twos_len):
        if twos[idx] == "0":
            tmp = twos[0:idx] + "1" +  twos[idx+1:twos_len]
            # print(twos, idx, tmp)
            # 2진수를 10진수로 변경
            sub = 1
            ans = 0
            for i in range(-1, -twos_len-1, -1):
                tt = int(tmp[i])
                ans = ans + sub * tt
                sub = sub * 2
                # print(tmp, ans)
            twos_lst.append(ans)
            


        elif twos[idx] == "1":
            tmp = twos[0:idx] + "0" +  twos[idx+1:twos_len]
            # 2진수를 10진수로 변경
            sub = 1
            ans = 0
            for i in range(-1, -twos_len-1, -1):
                tt = int(tmp[i])
                ans = ans + sub * tt
                sub = sub * 2
            twos_lst.append(ans)
        print(tmp, ans)
    print(twos_lst)

    # print("twos_lst", twos_lst)

    for idx in range(threes_len):
        for thr in ["0", "1", "2"]:
            if threes[idx] == thr:
                pass
            else:
                tmp = threes[0:idx] + thr + threes[idx+1:threes_len]

                # 3진수를 10진수로 변경
                sub = 1
                ans = 0
                for i in range(-1, -threes_len-1, -1):
                    tt = int(tmp[i])
                    ans = ans + tt * sub
                    sub = sub * 3

                threes_lst.append(ans)
                print(tmp, ans)
                # print(ans)

    print(threes_lst)
            # if ans in twos_lst:
            #     print(f"#{test_num} {ans}")
            #     break
        

                # print(ans)

    # print(twos_lst)