import sys

sys.stdin = open("default.txt")

# 10807
# n = int(input())
# lst = list(map(int, input().split()))
# m = int(input())
# ans = 0
# for i in lst:
#     if m == i:
#         ans += 1
# print(ans)

# 10871
# n, x = map(int, input().split())
# lst = list(map(int, input().split()))
# ans = ""
# for i in lst:
#     if i < x:
#         if ans == "":
#             ans = str(i)
#         else:
#             ans = ans + " " + str(i)
# print(ans)

# 10818
# n = int(input())
# lst = list(map(int, input().split()))
# min = 1000000
# max = -1000000
# for i in lst:
#     if min > i:
#         min = i
#     if max < i:
#         max = i
# print(min, max)

# 2562
# max = 0
# idx = 1
# while True:
#     try:
#         a = int(input())
#         if max < a:
#             max = a
#             ans = idx
#         idx += 1
#     except EOFError:
#         break
# print(max)
# print(ans)

# 5597
# lst = [0] * 31
# for _ in range(28):
#     a = int(input())
#     lst[a] = 1
# for i in range(1, 31):
#     if lst[i] == 0:
#         print(i)

# 3052
# a = set()
# for _ in range(10):
#     i = int(input())
#     a.add(i % 42)
# print(len(a))

# 1546
# n = int(input())
# lst = list(map(int, input().split()))
# max = 0
# for i in lst:
#     if max < i:
#         max = i
# for i in range(n):
#     lst[i] = lst[i]/max*100
# sum = 0
# for i in lst:
#     sum = sum + i
# ans = sum / n
# print(ans)

# 8958
# tc = int(input())
# for _ in range(tc):
#     lst = list(input())
#     cont = 0
#     ans = 0
#     for i in lst:
#         if i == "X":
#             cont = 0
#         else:
#             cont += 1
#             ans = ans + cont
#     print(ans)

# 4344
tc = int(input())

for _ in range(tc):
    lst = list(map(int, input().split()))

    mean = 0
    for i in lst[1:]:
        mean = mean + i
    mean = mean / lst[0]

    num = 0
    for i in lst[1:]:
        if i > mean:
            num += 1
    ans = num/lst[0]*100
    #     ans = ans + "%"
    print(f"{ans:.3f}%")