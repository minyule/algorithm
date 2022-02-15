import sys
sys.stdin = open("sample_input(2).txt")


quest = int(input())
 
for quest_num in range(quest):
    start = 1 # 시작 쪽 수
    end, A, B = map(int, input().split())
    #end = end -1 # 끝 쪽수
    # end = end + 1
    startA = start
    endA = end
    tryA = 0
 
    startB = start
    endB = end
    tryB = 0
 
 
    while startA <= endA:
        midA = (startA + endA) // 2
        tryA = tryA+1
        if midA < A: # mid가 큰 경우 start를 mid + 1로
            startA = midA
        elif midA > A: # mid가 작은 경우 end를 mid - 1로
            endA = midA
        else: # mid가 A 인 경우
            break
            # startA = midA
            # endA = midA
 
    while  startB <= endB:
        midB = (startB + endB) // 2
        tryB = tryB +1
        if midB < B: # mid가 큰 경우 start를 mid + 1로
            startB = midB
        elif midB > B: # mid가 작은 경우 end를 mid - 1로
            endB = midB
        else: # mid가 A 인 경우
            break
            # startB = midB
            # endB = midB
    # anser
    if tryA == tryB:
        print(f'#{quest_num+1} 0')
    elif tryA < tryB:
        print(f'#{quest_num+1} A')
    else:
        print(f'#{quest_num+1} B')


# quest = int(input())

# for quest_num in range(quest):
#     start = 1 # 시작 쪽 수
#     end, A, B = map(int, input().split())
#     # end = end -1 # 끝 쪽수
#     # end = end + 1
#     startA = 1
#     endA = end
#     tryA = 0

#     startB = 1
#     endB = end
#     tryB = 0

#     lst = [int(num) for num in range(1, end+1)]

#     while startA <= endA:
#         midA = (startA + endA) // 2
        
#         if lst[midA-1] < A: # mid가 큰 경우 start를 mid + 1로
#             startA = midA 
#             tryA = tryA + 1
#         elif lst[midA-1] > A: # mid가 작은 경우 end를 mid - 1로
#             endA = midA
#             tryA = tryA + 1
#         elif lst[midA-1] == A: # mid가 A 인 경우
#             break
#             # startA = midA
#             # endA = midA
#         # print(lst[midA-1], A)

#     while startB <= endB:
#         midB = (startB + endB) // 2
        
#         if lst[midB-1] < B: # mid가 큰 경우 start를 mid + 1로
#             startB = midB
#             tryB = tryB + 1
#         elif lst[midB-1] > B: # mid가 작은 경우 end를 mid - 1로
#             endB = midB
#             tryB = tryB + 1
#         elif lst[midB-1] == B: # mid가 B 인 경우
#             break
#             # startB = midB
#             # endB = midB
# # anser
#     if tryA == tryB:
#         print(f'#{quest_num+1} 0')
#     elif tryA < tryB:
#         print(f'#{quest_num+1} A')
#     else:
#         print(f'#{quest_num+1} B')
