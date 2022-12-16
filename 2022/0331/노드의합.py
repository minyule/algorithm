import sys
sys.stdin = open("노드의합.txt")

testcase = int(input())

def tree(N): # N번 자리의 값을 알고 싶어요
        
        if N*2+1 <= node:
            return tree(N*2) + tree(N*2+1) # 자식들의 합이에요

        elif N*2 <= node:
            return tree(N*2)

        else: # 자식이 없으면요
            return lst[N]

for test_num in range(1, testcase+1):

    node, leaf, result = map(int, input().split())

    lst = [None] + [0] * node

    for _ in range(leaf):
        idx, num = map(int, input().split())
        lst[idx] = num

    print(f'#{test_num} {tree(result)}')