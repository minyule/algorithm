import sys
sys.stdin = open("이진수.txt")

dic = {
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15
}

testcase = int(input())
for test_num in range(1, testcase+1):


    N, nums = input().split()


    ans = ""
    for num in nums:
        if num.isdecimal(): # 숫자면
            tmp = num
        else: # 숫자가 아니면
            tmp = dic[num]
        tmp = int(tmp)

        bin_num = ""
        for _ in range(4): # 2진수로 변경
            bin_num = str(tmp % 2) + bin_num
            tmp = tmp // 2
        ans = ans + bin_num
    print(f"#{test_num} {ans}")




    # ans = ""


    # for _ in range(4):
        