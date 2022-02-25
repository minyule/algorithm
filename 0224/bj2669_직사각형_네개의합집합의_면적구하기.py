


# # 베이스로 사용할 리스트 만듦. 0으로 채워져있음.
# base_lst = []
# for _ in range(100):
#     one_lst = []
#     for _ in range(100):
#         one_lst.append(0) 
#     base_lst.append(one_lst)


# for _ in range(4):
#     # lst.append(list(map(int, input().split())))
#     lst = list(map(int, input().split())) # lst 왼쪽아래x, y 오른쪽 위 x, y

#     for x_idx in range(lst[0], lst[2]):
#         for y_idx in range(lst[1], lst[3]):
#             base_lst[y_idx][x_idx] = 1

# ans = 0
# for ones in base_lst:
#     for one in ones:
#         ans = ans + one

# print(ans)


#----------------------

ans_set = set()
for _ in range(4):
    # lst.append(list(map(int, input().split())))

    lst = list(map(int, input().split())) # lst 왼쪽아래x, y 오른쪽 위 x, y

    for x_idx in range(lst[0], lst[2]):
        for y_idx in range(lst[1], lst[3]):
            # print([x_idx, y_idx])
            ans_set.add((x_idx, y_idx))

print(len(ans_set))
