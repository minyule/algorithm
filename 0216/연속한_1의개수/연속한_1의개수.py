import sys
from unicodedata import decimal
sys.stdin = open("input1.txt")

quest = int(input())

for quest_num in range(quest):

    N = int(input())
    max = 0
    lst = set(input().split("0"))
    # lst.remove("")
    # lst = list(lst)

    # ans = int("0b" + lst[-1], 2)
    # 연속으로 위치한 1로 이루어진 이진수 중 최댓값을 찾아버림

    lst = list(lst)
    for i in range(len(lst)):
        if len(lst[i]) > max:
            max = len(lst[i])

    print(f'{quest_num +1} {max}')
