from pprint import pprint
import sys
sys.stdin = open("미로_input.txt")

testcase_num = int(input())

map_lst = []

for _ in range(15):
    map_one = []
    line = input()
    for i in line:
        map_one.append(int(i))
    map_lst.append(map_one)

pprint(map_lst)

