import sys
sys.stdin = open("1312.txt")

a, b, c = map(int, input().split())
for _ in range(c):
    a = a % b * 10
    ans = a // b
print(ans)

