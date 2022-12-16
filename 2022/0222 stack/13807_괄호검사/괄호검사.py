# 스택 사용하기
# 열려있을때ㅐ( push
# peek 해서 비교하고, 닫히면) pop


import sys
sys.stdin = open("sample_input(1).txt")

quest = int(input())

for quest_num in range(1, quest+1):

    inp_string = input()

    stack = []

    brack = ["(", ")", "{", "}"]
    # open_brac = ["(", "{"]

    for letter in inp_string:

        if letter in brack:

            if letter == "(" or letter == "{": # 여는 괄호면
                stack.append(letter) # stack add
                
            elif letter == ")":
                if len(stack) == 0: # 스택에 아무것도 없으면
                    stack.append(letter) # 그냥 넣음
                elif stack[-1] == "(": # 스택에 뭐 있고, 마지막이 여는 소괄호면
                    stack.pop() # 뺌 
                else:
                    stack.append(letter)

                
            elif letter == "}":
                if len(stack) == 0: # 스택에 아무것도 없으면
                    stack.append(letter) # 그냥 넣음
                elif stack[-1] == "{": # 스택에 뭐 있고, 마지막이 여는 소괄호면
                    stack.pop() # 뺌
                else:
                    stack.append(letter) 



            elif len(stack) == 0: # 스택에 아무것도 없으면
                stack.append(letter) # 그냥 넣어줌

    if len(stack) > 0:
        ans = 0
    else:
        ans = 1

    print(f'#{quest_num} {ans}')