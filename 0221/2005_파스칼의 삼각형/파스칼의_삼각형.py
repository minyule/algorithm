import sys
sys.stdin = open("input.txt")

quest = int(input())

for quest_num in range(1, quest+1):

    N = int(input())


    def pascal(N):
        if N == 0:
            return []
        elif N == 1:
            return [[1]]
        else:
            output = [1]

            input = pascal(N - 1)
            input_last = input[-1]

            for i in range(len(input_last) - 1):
                output.append(input_last[i] + input_last[i+1])

            output = output + [1]
            input.append(output)

        return input


    print(f'#{quest_num}')

    # print(pascal(N))
    for n in pascal(N):
        
        for m in n:
            print(m, end=" ")
        print()
        

    


















# def pascal(input_lst):
#     if n == 1:
#         return [1]
    
#     else:
#         output_lst = [1]

#         for i in range(0, len(input_lst)-1):
#             output_lst.append(input_lst[i] + input_lst[i+1])

#         return output_lst


# memo = [0, 1]


# def pascal(lst):
#     if len(lst) == 1:
#         return lst
#     else:
#         input = [0] + pascal(N-1)

#         output = []
#         for i in range(len(input) - 1):
#             output.append(input[i] + input[i+1])
#         return output










# def pascal(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(pascal(n-1) + pascal(n-2))

#     return memo[n]

# memo = [0, 1]

# print(pascal(6))