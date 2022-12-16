import sys
sys.stdin = open("이진수2.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    num = float(input())
    # print(num)

    ans = ""
    sub = 0.5

    for _ in range(12):
        tmp = num - sub

        if tmp > 0:
            num = tmp
            ans = ans + "1"
        elif tmp < 0:
            ans = ans + "0"
        else:
            num = tmp
            ans = ans + "1"
            break
        sub = sub * 0.5
        # print(num)

    if num != 0:
        print(f"#{test_num} overflow")
    else:
        print(f"#{test_num} {ans}")