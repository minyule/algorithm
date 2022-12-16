import sys
sys.stdin = open("input.txt")

quest = int(input())

for quest_num in range(quest):
    bound = int(input())
    lst = []
    for _ in range(bound):
        one_lst = [0] + list(map(int, input().split())) + [0]
        lst.append(one_lst)

     # 이웃한 요소가 없을 경우 대비하여 상하좌우에 0으로 된 칸 넣어놨워요
    lst = [[0] * (bound+1)] + lst +[[0] * (bound+1)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    ans = 0

    for i in range(1, bound+1):
        for j in range(1, bound+1):
            for k in range(4): # 델타 사용했워요
                nx = j + dx[k]
                ny = i + dy[k]
                minu = lst[i][j] - lst[ny][nx]
                if 0<nx<(len(lst)-1) and 0<ny<(len(lst)-1):
                # nx == 0 or ny == 0 or nx == (len(lst)-1) or ny == (len(lst)-1):
                #     minu = 0
                # 뺸거 절댓값 씌우기
                    if minu >= 0:
                        ans = ans + minu
                    else:
                        ans = ans - minu
    print(f'#{quest_num} {ans}')