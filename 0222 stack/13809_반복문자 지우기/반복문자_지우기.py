import sys
sys.stdin = open("sample_input(3).txt")

quest = int(input())

for quest_num in range(1, quest + 1):

    inp_string = input()

    stack = []

    for one in inp_string:
        
        if len(stack) > 0: # 스택이 쌓여있으면
            if stack[-1] == one: # 같은 문자 연속 : 뺌
                stack.pop()

            else: # 연속 x : 추가
                stack.append(one)
                
        else: # 스택에 있는게 없으면 : 추가
            stack.append(one)

    print(f'#{quest_num} {len(stack)}')