import sys
sys.stdin = open("사칙연산.txt")

def calculate(a, cal, b):
    if cal == "+":
        return int(a)+int(b)
    elif cal == "-":
        return int(a)-int(b)
    elif cal == "*":
        return int(a)*int(b)
    elif cal == "/":
        return int(a)/int(b)

testcase = 10
for test_num in range(1, testcase +1):


    N = int(input())

    infos = [None]

    for _ in range(N):
        one_line = list(input().split())
        
        one_line[0] = int(one_line[0])
        if len(one_line) == 4:
            one_line[2] = int(one_line[2])
            one_line[3] = int(one_line[3])

        infos.append(one_line)



    ans_lst = [None] + [0] * N
    def tree(N):
        if len(infos[N]) == 2:
            ans_lst[N] = infos[N][1]

        elif len(infos[N]) == 4:
            ans_lst[N] = calculate( ans_lst[infos[N][2]] , infos[N][1] , ans_lst[infos[N][3]] )

        return(ans_lst)

    for i in range(N, 0, -1):
        tree(i)

    print(f"#{test_num} {int(ans_lst[1])}")


# 재귀로 풀고싶었는데, 
# 밑 코드를 보면 알겠지만, 리스트를 [2, -, 4, 5] 이런 꼴로 저장하고
# 재귀로 [2, 45] 라고 바꿔도 
# [2, -, 4, 5]라고 기억하고 있어서 해결을 못했음..



# 자식 있는 부모를 자식 계산한 숫자로 바꿔주기
# for info in infos:
#     if len(info) == 4:

# print(lst[2][0], calculate(lst[2],lst[1],lst[3]))
# print(infos[2][0], infos[2], infos[1], infos[3])


# print(lst)
# print(infos)




# ans_lst = [0] * N
# def tree(N):
#     # global infos
#     # return len(infos[N])
#     if len(infos[N]) == 2:
#         # if N == 1:
#         #     return infos[1][1]

#         print(10, infos, infos[N])

#         ans_lst[N] = infos[N][1]
#         # return tree(1)
#         return ans_lst[N]

#     elif len(infos[N]) == 4:
#         print(30, infos[N])
#         ans_lst[N] = calculate(tree(ans), infos[N][1], tree(infos[N][3]))
#         # infos[N] = [infos[N][0], calculate(tree(infos[N][2]), infos[N][1], tree(infos[N][3]))]
#         # infos[N] = [infos[N][0], calculate(tree(infos[infos[N][2]][0]), infos[N][1], tree(infos[infos[N][3]][0]))]
#         print(20, infos, infos[N],  N)
#         return ans_lst
#                 # infos[N][0]
# print(tree(1))
# # print(infos[2])
# # print(infos[infos[1][2]][0])

# N = 2
# print(calculate(infos[infos[N][2]][1], infos[N][1], infos[infos[N][3]][1]))

# print(len(infos[1]))


# infos[2] = [infos[2][0], calculate(infos[infos[2][2]][1], infos[2][1], infos[infos[2][3]][1])]

# N = 2    
# a = calculate(infos[infos[N][2]][1], infos[N][1], infos[infos[N][3]][1])
# print(a)



# print(infos)