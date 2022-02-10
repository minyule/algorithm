total_Q = int(input())
lst=[]
qus_num = 1
for _ in range(total_Q * 2):
    lst1 = list(map(int, input().split()))
    lst.append(lst1)

for lt in range(0, len(lst), 2):
    # lst[lt]는 개수 ex 5, 5, 10
    max = lst[lt + 1][0]
    min = lst[lt + 1][0]

    for one in range(lst[lt][0]):
        nums_lst = lst[lt+1]
        if max < nums_lst[one]:
            max = nums_lst[one]
        if min > nums_lst[one]:
            min = nums_lst[one]

    ans = max - min
    print("#{0} {1}".format(qus_num, ans))
    qus_num += 1

