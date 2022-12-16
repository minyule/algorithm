import sys
sys.stdin = open("input.txt")


for test_num in range(1, 11):

    node_cnt, line_cnt = map(int, input().split())

    lines = []  # node 번호가 인덱스고, 거기에 갈 수 있는 곳의 리스트를 넣어줄거야 
    # [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9]]
    for _ in range(node_cnt + 1):
        lines.append([])

    mid_affair = set() # 시작 위치가 아닌 곳

    inp_lst = list(map(int, input().split()))
    for i in range(0, len(inp_lst), 2):
        lines[inp_lst[i]].append(inp_lst[i+1])
        mid_affair.add(inp_lst[i+1])

    start_node = [] # 시작할 곳 정해요 (여기로 오는 곳은 아무데도 없어요)
    for s in range(node_cnt):
        if s not in mid_affair:
            start_node.append(s)

    start_node.pop(0)
    # start_node (시작점) 구했음 여기서 0은 무시함. 인덱스 위치 맞춰주려는 빈공간이야. -> 0 뺌

    visited = [] # 했던 일 기록

    stack = [] # 현재 가고 있는 길



    # 시작점 스택에 넣음
    for go_1 in range(len(start_node)):
        stack.append(start_node[go_1]) # start_node에 있는 것을 처음부터 순서대로 넣어줘요
        visited.append(start_node[go_1])



        # 스택 마지막 점에서 가는 것이 없으면 스택에서 빼버림
        while stack: 
            
            # 다음으로 갈 곳이 있으면
            for node in lines[stack[-1]]:
                # if len(lines[stack[-1]]) != 0 and  not in visited:
                
                if len(lines[stack[-1]]) > 0 and node not in visited:
                    stack.append(node)
                    visited.append(node)
                    break

            else:

                stack.pop()
                # 방문한 곳이 아니어야해
                # if lines[stack[-1]] not in visited:
                #     stack.append(lines[stack[-1]])
                #     visited.append(lines[stack[-1]])

    print(f'#{test_num}', end=" ")
    print(*visited)
            




