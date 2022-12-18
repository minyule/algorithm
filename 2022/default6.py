import sys

sys.stdin = open("default.txt")
# 11654
# a = input()
# print(ord(a))

# 11720
# a = int(input())
# lst = list(input())
# ans = 0
# for i in lst:
#     ans = ans + int(i)
# print(ans)

# 10809
# s = input()
# ans = [-1] * 26
# ing = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#        "w", "x", "y", "z"]
# for i in range(26):
#     for wi in range(len(s)):
#         if ing[i] == s[wi]:
#             ans[i] = wi
#             break
#
# a = str(ans[0])
# for i in range(1, 26):
#     a = a + " " + str(ans[i])
# print(a)

# 2675
# tc = int(input())
# an_lst = []
# for _ in range(tc):
#     a, b = input().split()
#     a = int(a)
#     an = ""
#     for i in b:
#         an = an + i * a
#     an_lst.append(an)
# for i in an_lst:
#     print(i)

# 1157
# a = input()
# lst = [0] * 91
# for i in a:
#     b = ord(i)
#     if b >= 97:
#         b = b - 32
#     lst[b] = lst[b] + 1
# max = 0
# for i in range(91):
#     if max < lst[i]:
#         max = lst[i]
#         ans = chr(i)
#     elif max == lst[i]:
#         ans = "?"
# print(ans)

# 1152
# 이전에 푼 문제

# 2908
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# ans = a
# if b > a:
#     ans = b
# print(ans)

# 5622
# a = input()
# ans = 0
# for i in a:
#     i = ord(i)
#     if 65 <= i <= 67:
#         ans = ans + 3
#     elif 68 <= i <= 70:
#         ans = ans + 4
#     elif 71 <= i <= 73:
#         ans = ans + 5
#     elif 74 <= i <= 76:
#         ans = ans + 6
#     elif 77 <= i <= 79:
#         ans = ans + 7
#     elif 80 <= i <= 83:
#         ans = ans + 8
#     elif 84 <= i <= 86:
#         ans = ans + 9
#     elif 87 <= i <= 90:
#         ans = ans + 10
# print(ans)

# 2941
# one_lst = ["c", "d", "l", "n", "s", "z"]
# two_lst = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
# three_lst = "dz="
# a = input()
# no = 0
# for i in range(len(a)):
#     if a[i] in one_lst:
#         if a[i:i+3] == three_lst or a[i:i+2] in two_lst:
#             no = no + 1
# print(len(a) - no)

# 1316
# tc = int(input())
# ans = 0
# for _ in range(tc):
#     a = input()
#     lst = [a[0]]
#     for i in range(1, len(a)):
#         if a[i] in lst:
#             if a[i-1] == a[i]:
#                 pass
#             else:
#                 # 연속아님
#                 ans -= 1
#                 break
#         else:
#             lst.append(a[i])
#     ans += 1
# print(ans)