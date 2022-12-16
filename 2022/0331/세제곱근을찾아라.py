import sys
sys.stdin = open("세제곱근을찾아라.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):
    num = int(input())
    ans = -1

    for i in range(1, (num**(1/2))//2):
        triple = i * i * i
        
        if triple == num:
            ans = i
            break

    print(f'#{test_num} {ans}')






# for test_num in range(1, testcase + 1):
#     num = int(input())

#     triple = num ** (1/3)
#     print(triple)
#     if triple == int(triple):
#         print(int(triple))
#     else:
#         print(-1)


# print(triple == int(triple))

# if type(num**(1/3)) == int:
#     print(num)