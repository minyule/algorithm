import sys

sys.stdin = open("default.txt")

# 2739
# a = int(input())
# for i in range(1, 10):
#     print(a, "*", i, "=", a*i)

# 10950
# tc = int(input())
# for _ in range(tc):
#     a, b = map(int, input().split())
#     print(a + b)

# 8393
# a = int(input())
# ans = 0
# for i in range(a+1):
#     ans = ans + i
# print(ans)

# 25304
# res = int(input())
# tc = int(input())
# ans = 0
# for _ in range(tc):
#     a, b = map(int, input().split())
#     ans = ans + a * b
# if res == ans:
#     print("Yes")
# else:
#     print("No")

# 15552
# tc = int(sys.stdin.readline().rstrip())
# for _ in range(tc):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     print(a + b)

# 11021
# tc = int(input())
# for i in range(1, tc + 1):
#     a, b = map(int, input().split())
#     print("Case #" + str(i) + ":", a+b)

# 11022
# tc = int(input())
# for i in range(1, tc + 1):
#     a, b = map(int, input().split())
#     print("Case #" + str(i) + ":", a, "+", b, "=", a + b)

# 2438
# a = int(input())
# for i in range(1, a+1):
#     print("*" * i)

# 2439
# a = int(input())
# for i in range(1, a + 1):
#     print(" " * (a - i) + "*" * i)

# 10952
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a + b)

# 10951
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except EOFError:
#         break

# 1110
# a = input()
# ans = 1
# if int(a) < 10:
#     a = "0" + a
# while True:
#     nxt = int(a[-1]) + int(a[-2])
#     if nxt >= 10:
#         nxt = nxt - 10
#     a = a + str(nxt)
#     if a[0] == a[-2] and a[1] == a[-1]:
#         break
#     ans += 1
# print(ans)
