from re import sub
import sys
sys.stdin = open("이진탐색.txt")

testcase = int(input())


# for test_num in range(1, testcase + 1):

N = int(input())

lst = [None]
lst.extend([0 for _ in range(N)])

depth = 1
subject = 2

while subject / N < 1:
    subject = subject * 2
    depth = depth + 1

length = 2 ** depth

print(lst)
print(depth, length)