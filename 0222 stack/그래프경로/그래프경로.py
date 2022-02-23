import sys
sys.stdin = open("sample_input(2).txt")

quest = int(input())

for quest_num in range(1, quest+1):

    # V : node, E : line
    V, E = map(int, input().split())

    # 비어있는 2차원 리스트 만들었워요
    line_lst = []
    for _ in range(V):
        empty = []
        line_lst.append(empty)

    stack = []
    visited = []

    # 각 노드에서 이어지는 곳을 line_lst에 추가해줌. (1에서 이어지는 곳은 인덱스 1인 곳의 리스트에 추가해줌)
    # [[], [4, 3], [3, 5], [], [6]]
    for _ in range(E):  # add line
        node, line = map(int, input().split())
        line_lst[node].append(line)

    # 시작점과 끝점 입력받음
    start, end = map(int, input().split())

    stack.append(start) # 스택에 시작점 넣어줌
    visited.append(start) # 갔던 곳 저장


    while stack: # 스택에 값이 존재한다면) 계속 반복
        tmp = stack[-1]

        if len(line_lst[tmp]) > 0:
            for node in line_lst[tmp]:
                
                if node not in visited:
                    stack.append(node)
                    visited.append(node)
                    break
                print(stack, visited)
            
            else:
                stack.pop()
        else:
            stack.pop()
 
        # print(visited, stack)
    # print(f"#{quest_num} {ans}")






















    #    try:

            

    #         if len(line_lst[stack[-1]]) == 0: # 갈 수 있는 곳이 없으면
    #             # 스택에서 마지막 루트 빼버리고
    #             stack.pop()

    #             line_lst[stack[-1]].pop() #????????????? 그 길로가는 거 없애야하는디
    #             # 그 잘못된 도착지도 빼버려야함. 그 다음 목적지 추가해야함
    #             stack.append(line_lst[stack[-1]][-1])
                

    #         elif line_lst[stack[-1]][-1] in stack:  # 자기 자신으로 돌아오게 된다면
    #             line_lst[stack[-1]].pop()
    #         # elif line_lst[line_lst[stack[-1]][-1]][-1] == stack[-1]: 
    #         #     line_lst[stack[-1]].pop()

    #         # 스택의 마지막 부분(stack[-1])에서 갈 수 있는 곳(line_lst[stack[-1]])을 순서대로 가본다.
    #         else:
    #             stack.append(line_lst[stack[-1]][-1]) # 갈수있는 곳의 맨 뒤에꺼 넣어주기. pop하기 쉽게
    #             ans = 1

            
                

    #         if len(line_lst[start]) == 0:
    #             ans = 0
    #             break


    #     except: # 에러발생하면
    #         ans = 0
    #         break
        
    #     print(stack, line_lst)