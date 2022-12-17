import sys
sys.stdin = open("default.txt")

# 1330
# a, b = map(int, input().split())
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("==")

# 9498
# a = int(input())
# if 90 <= a <= 100:
#     print("A")
# elif 80 <= a <= 89:
#     print("B")
# elif 70 <= a <= 79:
#     print("C")
# elif 60 <= a <= 69:
#     print("D")
# else:
#     print("F")

# 2753
# a = int(input())
# if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#     print(1)
# else:
#     print(0)

# 14681
# a = int(input())
# b = int(input())
# if a > 0:
#     if b > 0:
#         print(1)
#     else:
#         print(4)
# elif a < 0:
#     if b > 0:
#         print(2)
#     else:
#         print(3)

# 2884
# a, b = map(int, input().split())
# if b >= 45:
#     b = b - 45
# else:
#     a = a - 1
#     if a < 0:
#         a = a + 24
#     b = b + 60 - 45
# print(a, b)

# 2525
# a, b = map(int, input().split())
# c = int(input())
# b = b + c
# while b >= 60:
#     b = b - 60
#     a = a + 1
# if a >= 24:
#     a = a - 24
# print(a, b)

# 2480
# a, b, c = map(int, input().split())
# if a == b == c:
#     ans = 10000 + a * 1000
# elif a == b:
#     ad = a
#     ans = 1000 + ad * 100
# elif b == c:
#     ad = b
#     ans = 1000 + ad * 100
# elif a == c:
#     ad = c
#     ans = 1000 + ad * 100
# else:
#     mx = a
#     if mx < b:
#         mx = b
#     if mx < c:
#         mx = c
#     ans = mx * 100
# print(ans)
