
import sys
sys.stdin = open("최소합.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    N = int(input())

    map_lst = []
    for _ in range(N):
        map_lst.append(list(map(int, input().split())))

    # print(map_lst)

    order_lst = [0 for _ in range(2*N-2)]

    # [0, 1, 2, 3] 중에 랜덤으로 두 개를 뽑기
    lst_for_combi = []
    for i in range(2*N-2):
        lst_for_combi.append(i)

    # 2개 뽑는 조합
    combi_lst = []
    r = N-1
    def make_combi(combi):

        if len(combi) == r: # 길이가 2면 끝내기
            combi_lst.append(combi[:])
            return

        for i in lst_for_combi:
            if combi and i <= max(combi): # 리스트가 있는데, 리스트 안에 있는 최대값보다 작으면 넣지않음(sort된 상태이므로)
                continue
            # 그 외의경우는 넣어준다.(리스트가 없어서 새로 넣어주는 경우랑 최댓값보다 큰 값 넣는 경우)
            combi.append(i)
            make_combi(combi)
            combi.pop()

    make_combi([])

    orders = []
    for combis in combi_lst:
        order_lst = [0 for _ in range(2*N-2)]
        for com in combis:
            order_lst[com] = 1
        # print(order_lst)
        orders.append(order_lst)
    # print(orders)


    # 0과 1로 이루어진 집합이 주어지면 가능한 코드.
    # 예를 들어 [[0, 0, 1, 1], [0, 1, 0, 1], ...]이런 식으로

    ans = 10000000000 # 더미 값

    # 위치이동 0오른쪽, 1아래
    dx = [1, 0]
    dy = [0, 1]

    for order in orders:
        # print(order)
        nx = 0
        ny = 0
        min = map_lst[ny][nx]

        for ord in order:
            nx = nx + dx[ord]
            ny = ny + dy[ord]
            min = min + map_lst[ny][nx]

        print(order, ans)
        if ans >= min:
            ans = min

    print(f"#{test_num} {ans}")
