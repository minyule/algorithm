# import sys
# sys.stdin = open("input.txt")



# quest = int(input())
# for quest_num in range(quest):
n = int(input())
into_snail = 0
lst = [[0] * n] * n
into_snail = 1
for one_row in range(n):
    lst[0][one_row] = into_snail
    into_snail = into_snail + 1

n = n-1
for i in range(n-1, 0, -1):
    for j in range(n):
        lst[j][i] = into_snail
        into_snail = into_snail + 1
        print(lst)
        exit



print(lst)



# # 0우 1하 2좌 3하
# dy = [1, 0, -1, 0]
# dx = [0, 1, 0, -1]

# ny = 0
# nx = 0
# into_snail = 1
# lst[ny][nx] = into_snail
# for _ in range(n*n - 1):

#     lst[ny + dy[k]][nx + dx[k]]

#     into_snail = into_snail + 1



# print(lst)





