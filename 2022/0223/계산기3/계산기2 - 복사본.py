from msilib.schema import Error
import sys
from turtle import st
sys.stdin = open("input.txt")

for textcase in range(1, 11):

    textcase_length = int(input())

    formula = input()

    isp = {"+": 1, "*": 2, "(":0} # stack안에 있을때 우선순위 +. *
    icp = {"+": 1, "*": 2, "(":3} # stack으로 들어올 때 우선순위 +, *

    subject = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    stack = [] 
    ans_string = "" # 출력할 값



    # 1. 피연산자는 스택에 바로 넣기
    for token in formula:
        if token in subject:
            ans_string = ans_string + token


        # 연산자의 경우, 
        else:
            # 연산자가 들어가는 스택이 비어있으면 넣어줌
            if len(stack) == 0:
                stack.append(token)
            
            
            # # 스택 맨 뒤에 피연산자가 있다면 그냥 넣어줌
            # if stack[-1] in subject:
            #     stack.append(token)

            # 스택 맨 뒤에 연산자가 있다면
            # 스택 연산자의 isp가 토큰의 icp보다 작으면 넣음  
            elif isp[stack[-1]] < icp[token]:
                stack.append(token)

            # 스택 연산자의 isp가 토큰의 icp보다 크거나 같으면
            # 스택 맨 뒤 연산자 isp가 작아지던지, 스택 길이가 0이 될 때까지 반복
            else:
                # while  isp[stack[-1]] >= icp[token]:
                # 스택 맨 뒤에꺼 빼서 출력에 넣어줌
                ans_string = ans_string + stack[-1]
                stack.pop()
                stack.append(token)

        # print(token, ans_string,  stack)
                
    # 마지막에 남은 연산자들을 출력값으로 넣어줌
    for _ in range(len(stack)):
        ans_string = ans_string + stack[-1]
        stack.pop()

    #---------------------계산할것임-----------------


    # ans_string을 계산하기
    for token in ans_string:
        # 피연산자면 스택에 넣어둠
        if token in subject:
            stack.append(token)

        # 피연산자면 스택에서 두개 꺼내고, 해당 연산 해서 ans에 저장해둠
        # 계산한 ans는 스택으로 다시 넣어줌
        else: 
            if token == "*":
                ans = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(ans)
            else:
                ans = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(ans)


    print(f'#{textcase} {ans}')





