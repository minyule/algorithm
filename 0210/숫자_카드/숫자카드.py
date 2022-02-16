total_Q = int(input())
lst=[]
qus_num = 1
for _ in range(total_Q):
    lst0 = [int(input())]
    lst1 = list(map(int, input()))
    lst.append(lst0)
    lst.append(lst1)
# lst = [[5], [4, 9, 6, 7, 9], [5], [0, 8, 2, 7, 1], [1, 0], [7, 7, 9, 7, 9, 4, 6, 5, 4, 3]]


for one_num in range(0, total_Q * 2, 2):
    normal_lst = [0] * 10  # 디폴트 리스트 만들어놓음
    # lst[one_num] : [5], [5], [10]
    for nums in range(lst[one_num][0]):
        normal_lst[lst[one_num+1][nums]] += 1
    # print(normal_lst)
    # normal_lst : [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # 개수가 최대인 곳의 값과 인덱스를 저장하고 답 출력
    max = normal_lst[0]
    ans_idx = 0
    for idx in range(len(normal_lst)):
        if max <= normal_lst[idx]:
            max = normal_lst[idx]
            ans_idx = idx
    print(f'#{qus_num} {ans_idx} {max}')
    # print("#{0} {1} {2}".format(qus_num, ans_idx, max))
    qus_num += 1