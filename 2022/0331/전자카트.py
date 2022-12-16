
import sys
sys.stdin = open("전자카트.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    N = int(input())

    map_lst = []
    for _ in range(N):
        map_lst.append(list(map(int, input().split())))


    order_lsts = []

    order_lst = [0]

    lst = [] # [1, 2]
    for i in range(1, N):
        lst.append(i)

    # 시작과 끝은 0이어야함. 01, 12, 20 처럼.
    # 여기서 가운데에 들어가는 1, 2의 숫서를 순열을 통해 구해줄 것임.

    r = N-1
    orders_lst = []
    def make_perm(perm):
        if len(perm) == r: # 길이 되면 중단
            orders_lst.append(perm[:])
            return
        for i in lst:
            if i not in perm: # 없으면
                perm.append(i) # 추가해주고
                make_perm(perm) # 있는 상태에서 순열만들기
                perm.pop() # 빼버리고 이후 없는 상태에서 순열 만들기
    make_perm([])
    # orders_lst = [[1,2], [2,1]]


    ans = 1e9 # 더미
    # 10^9를 뜻함

    for orders in orders_lst: # [1,2]에 대해서
        battery = 0
        nowY = 0 # 무조건 사무실에서 출발
        # [0,1] [1,2] [2,0] 처럼 도착지 번호가 출발지 번호로 옮겨져 감
        for order in orders: # 1이면
            nowX = order
            battery = battery + map_lst[nowY][nowX]
            nowY = nowX
            
        battery = battery + map_lst[nowY][0] # 마지막에 사무실에 들리기
        if ans > battery:
            ans = battery

    print(f"#{test_num} {ans}")