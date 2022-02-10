total_Q = int(input())
lst=[]
qus_num = 1
for _ in range(total_Q*2):
    lst1 = list(map(int, input().split()))
    lst.append(lst1)
# [[10,3][1,2,3,4,5,6,7,8,9,10] ... ] 이런 꼴로 입력받은 lst
for i in range(1, len(lst), 2):
    sum_nums = lst[i-1][1] # 더하는 숫자 개수
    num_lst = lst[i] # 숫자들 리스트 [1,2,3,...]

    # 맨 앞 숫자들의 합으로 sum_max, sum_min 초기화
    sum_max = 0
    sum_min = 0
    for sum_init in range(sum_nums):
        sum_max += num_lst[sum_init]
        sum_min += num_lst[sum_init]

    #가장 큰 값과 작은 값을 sum_max, sum_min에 각각 넣음
    for idx in range(0, len(num_lst) - sum_nums + 1):
        # 숫자들 합을 구함 sum_lit
        sum_lit = 0
        for sums in range(sum_nums):
            sum_lit += num_lst[idx + sums]
        # print(sum_lit)
        
        # sum_lit와 비교해서 큰값, 작은값 바꿈
        if sum_max < sum_lit:
            sum_max = sum_lit
        if sum_min > sum_lit:
            sum_min = sum_lit

    print(f'#{qus_num} {sum_max - sum_min}')
    qus_num += 1
