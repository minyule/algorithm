import sys
sys.stdin = open("이진힙.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    N = int(input())

    inp_lst = [None] + list(map(int, input().split()))

    base = []
    base.append(None)
    base.append(inp_lst[1])

    def change(now):
        # print(now)
        while now > 1 and base[now] < base[now//2] :
            tmp = base[now//2]
            base[now//2] = base[now]
            base[now] = tmp
            now = now//2

    for idx in range(2, len(inp_lst)):
        base.append(inp_lst[idx])
        change(idx)

    ans = 0

    idx = N
    while idx > 1:
        idx = idx // 2
        ans = ans + base[idx]
        
    print(f'#{test_num} {ans}')


# 시행착오
# 과정을 거꾸로 생각해서 미리 트리 값을 받은 다음에
# 맨 밑의 노드부터 올라가면서 작아지는지 확인하고 
# 크면 바꾸기를 했더니
# 이건 위에서부터 바꿔나가는것과 결과가 달랐다.
# 왼쪽 오른쪽 자식 선택되는 것 차이로 인한 것 같다.

# while 조건을 or로 했다가 and로 하니까 됨
# 
# 
# 
# 
# 
# #













# for test_num in range(1, testcase+1):

# N = int(input())

# inp_lst = [None] + list(map(int, input().split()))

# # 부모를 idx1로 놓고, 자식인 idx1*2, idx1*2+1랑 비교하려 했더니
# # 그러면 오른자식보다 왼손자랑 먼저 계산해버리는 불상사가 발생해요 
# # 
# # 틀림 음 왜냐면
# # 9 8 7 6 5 4 3 2 1 0 해보면 알겟지만
# # 만들어놓고 정리하면 나중에 들어온 애랑 안좋게 될수이슴

# def change(idx1): # idx1 (smaller), idx1+1 (bigger)
#     global N
#     if inp_lst[idx1//2] > inp_lst[idx1]: # des' value is bigger

#         tmp = inp_lst[idx1]
#         inp_lst[idx1] = inp_lst[idx1//2]
#         inp_lst[idx1//2] = tmp
#         return 1

#     return 0
# swit = 1
# while swit != 0:
#     swit = 0
#     for i in range(2, N+1): # 모든 번호 순회하면서 교환
#         swit = swit + change(i)


# ans = 0
# N = N // 2


# while N > 1:

#     ans = ans + inp_lst[N]

#     N = N // 2

# ans = ans + inp_lst[1]

# # print(f'#{test_num} {ans}')