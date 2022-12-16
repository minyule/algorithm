import sys
sys.stdin = open("subtree.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    node_cnt, start = map(int, input().split())

    base = [] # 트리 내용물 [[], [6], [1, 5], [], [], [3], [4]]
                # 0번째는 없는셈 치기
    for _ in range(node_cnt + 2):
        base.append([])

    inp_line = list(map(int, input().split()))
    for i in range(0, node_cnt * 2, 2):
        base[inp_line[i]].append(inp_line[i+1])

    # ---------입력받음---------------

    # start에서 시작해서

    # visited를 원래 개수만큼 만들어서 방문했으면 
    visited = []
    stack = []

    now = start
    visited.append(now)
    stack.append(now)

    swit = 0

    while swit != len(base[start]):

        # 자식이 없거나, 오른쪽 자식이 방문한적 있는 곳이면
        if len(base[now]) == 0 or base[now][-1] in visited:
            # 부모로
            stack.pop()
            now = stack[-1]
            if now == start:
                swit += 1


        # 왼쪽 자식이 방문한적 없는 곳이면
        elif base[now][0] not in visited:
            # 왼쪽으로 이동
            now = base[now][0]
            stack.append(now)
            visited.append(now)

        # 왼쪽 자식이 방문한 적 있는 곳이면
        else:
            # 오른쪽으로 이동
            now = base[now][1]
            stack.append(now)
            visited.append(now)

    print(f'#{test_num} {len(visited)}')

