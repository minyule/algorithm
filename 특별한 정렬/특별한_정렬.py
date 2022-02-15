import sys
sys.stdin = open("sample_input(3).txt")

quest = int(input())

for quest_num in range(quest):
    sample = int(input())
    lst = list(map(int, input().split()))
    lst_ans = []
    

    for _ in range(5):
        min = lst[0]
        for i_min in range(len(lst)):
            tmp = lst[i_min]
            if tmp < min:
                min = tmp

        max = lst[0]
        for i_max in range(len(lst)):
            tmp = lst[i_max]
            if tmp > max:
                max = tmp
        
        lst_ans = lst_ans + [max, min]
        lst.pop(lst.index(max))
        lst.pop(lst.index(min))

    
    print(f'#{quest_num+1}', *lst_ans)

# lst_ans = [0] * 10
# def find_n_min(lst, n):
#     for i in range(n-1):
#         minIdx = i
#         for j in range(i+1, n):
#             if lst[minIdx] > lst[j]:
#                 minIdx = j
#         lst[i], lst[minIdx] = lst[minIdx], lst[i]
#     return lst[minIdx]



#     find_n_min(lst, sample)
#     print(lst)

# def selectionSort(a, N):
#     for i in range(0, N):
#         minIdx = i
#         for j in range(i+1, len(a)):
#             if a[minIdx] > a[j]:
#                 minIdx = j
#         a[i], a[minIdx] = a[minIdx], a[i]
#     return a[minIdx-1]


# for quest_num in range(quest):
#     sample = int(input())
#     lst = list(map(int, input().split()))

#     lst_ans=[]


