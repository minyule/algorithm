import sys
sys.stdin = open("input.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    inp_money = int(input())

    money_kind = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    out_money = [] # 여기에 정답 입력해줄거에요

    for money in money_kind:

        out_money.append(inp_money // money)

        inp_money = inp_money % money

    # charge = inp_money // 50000

    # inp_money = inp_money % 50000

    print(f'#{test_num}')
    print(*out_money)