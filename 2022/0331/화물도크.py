import sys
sys.stdin = open("화물도크.txt")

# 하루 24시간동안 시간이 겹치지 않고 최대한 많은 화물차를 사용하기
# 1. 화물차 개수가 5개라면 [0, 1, 2, 3, 4]의 부분집합을 구함.숫자는 화물차의 번호라고 간주
# 2. 부분집합의 개수가 긴 것부터 사용 시간을 보고 불가능한 경우면 중지, 가능하면 그 떄의 부분집합 길이 반환
# 3. #

def make_combi(combi, idx):
    if len(combi) == r:
        total_lst.append(combi[:])
        return
    for i in range(idx+1, len(lst)):
        combi.append(lst[i])
        make_combi(combi, i)
        combi.pop()
        

testcase = int(input())

for test_num in range(1, testcase+1):

    N = int(input())

    start = []
    end = []
    for _ in range(N):
        s, e = map(int, input().split())
        start.append(s)
        end.append(e)

    lst = [i for i in range(N)] # [0, 1, 2, 3, 4]

    for i in range(N, 0, -1): # 길이가 긴 것부터 값을 구해봐요
        r = i
        total_lst = []
        make_combi([], -1)

        for orders in total_lst: # orders은 [0, 1, 2, 3, 4]와 같은 모양
            times = [0 for _ in range(24)]
            ans = True
            for order in orders: # order은 0부터 순서대로
                for time in range(start[order], end[order]):
                    if times[time] > 0 : # 못씀
                        ans = False
                        break
                    else:
                        times[time] = 1
            if ans:
                break
        if ans:
            real_ans = r
            break

    print(f"#{test_num} {real_ans}")





# print(lst)
