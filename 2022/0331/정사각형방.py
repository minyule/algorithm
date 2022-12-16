import sys
sys.stdin = open("정사각형방.txt")

# N^2 개의 방이 N * N 형태로 있음
# 방에는 수가 적혀있음.
# 상하좌우의 방으로 이동가능.
# 이동하려는 방에 적힌 숫자가 현재 방의 숫자보다 1 커야함
# 어떤 수가 적힌 방에서 시작해야 가장 많은 개수의 방을 갈 수 있는지 (중복된다면 최소값) 출력
# 해당 방에서 몇 개의 방을 이동 가능한지 출력 (자기자신 포함)#

testcase = int(input())

for test_num in range(1, testcase + 1):

    N = int(input())

    map_lst = []
    cnt_lst = [] # 여기에는 각 리스트의 칸에서 갈 수 있는 최대 값을 저장할 거임
    for _ in range(N):
        one_line = list(map(int, input().split()))
        map_lst.append(one_line)
        cnt_lst.append([0 for _ in range(N)])

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def count(nowx, nowy):
        check = -1
        nx = nowx
        ny = nowy
        while check != 0:
            check = 0
            for i in range(4):

                lx = nx + dx[i]
                ly = ny + dy[i]

                if 0 <= lx < N and 0 <= ly < N: # 리스트 범위 내에 있는지 확인
                    if map_lst[ly][lx] == map_lst[ny][nx] + 1: # 현재 방 + 1 확인
                        cnt_lst[nowy][nowx] += 1
                        nx = lx
                        ny = ly
                        check += 1 # 이걸 한번도 안거치면 볼 방 없단 것. while 멈춤
                        break
    max = 0
    max_min = N*N # 임의로 초기화
    for x in range(N):
        for y in range(N):
            count(x, y)
            if cnt_lst[y][x] > max:
                max = cnt_lst[y][x]
    for x in range(N):
        for y in range(N):
            if max == cnt_lst[y][x]:
                if map_lst[y][x] < max_min:
                    max_min = map_lst[y][x]


    print(f'#{test_num} {max_min} {max+1}')
    # print(f'# {max_min} {max+1}')

    # print(cnt_lst)            


# N*N개의 길이인 리스트를 만들고
# 그 리스트 인덱스(방에 쓰인 번호) 위치에 2차원리스트에서 방의 좌표를 저장
# ex. 1이 쓰인(인덱스가 1인곳에 저장된 좌표값 확인)
# 다음 2가 쓰인(인덱스가 2인 곳에 저장된 좌표값 확인하고), 
# 1인 곳과 2인곳 좌표 차이가 절대값 1인 경우 max 값 갱신하고~~ 과정#

