import sys
sys.stdin = open("최소신장트리.txt")

testcase = int(input())
for test_num in range(1, testcase + 1):
    node, line = map(int, input().split())

    node_lst = [[] for _ in range(node + 1)]
    # print(node_lst)

    for _ in range(line):
        s, e, d = map(int, input().split())
        # print(s, e, d)
        node_lst[s].append(d)
        node_lst[e].append(d)
    print(node_lst)
    












    # print(node_lst)
    # s, e, d = map(int, input().split())
    # node_lst[s] = 0
    # node_lst[e] = d

    # for _ in range(line-1):
    #     s, e, d = map(int, input().split())
    #     if node_lst[e] > d:
    #         node_lst[e] = d

    # print(node_lst)