
import sys
sys.stdin = open("재미있는_오셀로게임.txt")

# 8방 둘러보기용 리스트
#  0북, 1북동, 2동, 3남동, 4남, 5남서, 6서, 7북서
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

test_case = int(input())

for test_num in range(1, test_case + 1):

    N, M = map(int, input().split()) # N: 한변의길이, M: 돌 놓는 횟수

    # map_lst 만들기
    map_lst = []
    for _ in range(N):
        map_lst.append([0 for _ in range(N)])

    # 처음 돌 세팅
    map_lst[N//2][N//2] = 2
    map_lst[N//2 -1][N//2 -1] = 2
    map_lst[N//2][N//2 -1] = 1
    map_lst[N//2 -1][N//2] = 1

    # 돌 놓기
    for _ in range(M):


        # 임시저장할 리스트 (돌 놓기 전)
        # tmp_lst = map_lst[::]

        newX, newY, newStone = map(int, input().split())
        newX -= 1
        newY -= 1
        map_lst[newY][newX] = newStone
        # newStone과 반대 색깔의 색을 versusStone에 입력
        if newStone == 1:
            versusStone = 2
        else:
            versusStone = 1

        chec = 0
        # 8방을 둘러보기
        for direction in range(8):

            add_idx = []

            # 그 방향으로 쭉 가면서 체크한다.
            for distance in range(1, N):
                aroundX = newX + dx[direction] * distance
                aroundY = newY + dy[direction] * distance
                # 인덱스 범위 넘어가면
                if not (0 <= aroundX < N and 0 <= aroundY < N):
                    break

                # 인덱스 범위 넘어가지 않고
                else:
                    # 다른색돌이면 색깔 바꿔줄 인덱스 리스트에 추가
                    if map_lst[aroundY][aroundX] == versusStone:
                        add_idx.append([aroundY, aroundX])
                        # print(add_idx)

                    # 같은색돌이 나오면 색깔 바꿔줄 리스트 값들 바꿔줌
                    elif map_lst[aroundY][aroundX] == newStone:
                        
                        for idx in add_idx:
                            map_lst[idx[0]][idx[1]] = newStone
                            chec += 1
                        add_idx = []
                        
                        break
                    # 비어있는 칸이 나오면, X나 Y좌표가 가장자리로 가면 (같은색돌 나오기 전임) 저장하기 전 map_lst가져옴
                    else: 
                        # map_lst[newY][newX] = 0
                        break
        #             print(add_idx)
        #     print("chec", chec)
        # print(newX, newY)
        if chec == 0:
            map_lst[newY][newX] = 0
        chec = 0
        
        # add_idx = []
        
        # print(map_lst)


    blackCnt = 0
    whiteCnt = 0
    for X in range(N):
        for Y in range(N):
            if map_lst[Y][X] == 2:
                whiteCnt += 1
            elif map_lst[Y][X] == 1:
                blackCnt +=1
    # print(map_lst)
    print(f"#{test_num} {blackCnt} {whiteCnt}")

# 실수 1.
# 마지막 개수 셀 때, 2이면 흰돌, 나머지는 검은돌 했다가
# 0도 검은돌로 세어져서 ㅇㅇ..#

# lst1 = [1, 2, 3]
# lst2 = lst1[::]
# lst2[0] = 2
# print(lst1)









# 8방을 둘러보기
# for direction in range(8):
#     aroundX = newX + dx[direction]
#     aroundY = newY + dy[direction]

#     # tmp_lst를 벗어나지 않았다면,
#     if 0 <= aroundX < N and 0 <= aroundY < N:
#         if tmp_lst[aroundY][aroundX] == versusStone: # 다른 색의 돌과 마주하고 있다면
#             # 해당 방향으로 쭉 가면서 체크할 것.
#             for distance in range(2, N):
#                 endStoneX = newX + dx[direction] * distance
#                 endStoneY = newY + dy[direction] * distance
#                 # 인덱스 범위 넘어가지 않고
#                 if 0 <= endStoneX < N and 0 <= endStoneY < N:
#                     # 다른색돌이면 색깔 바꿔줌
#                     if tmp_lst[endStoneY][endStoneX] == versusStone:
#                         tmp_lst[endStoneY][endStoneX] = newStone
#                     # 같은색돌이 나오면 지금까지 상태를 map_lst에 저장
#                     elif tmp_lst[endStoneY][endStoneX] == newStone:
#                         map_lst = tmp_lst
#                     # 비어있는 칸이 나오면 (같은색돌 나오기 전임) 저장하기 전 map_lst가져옴
#                     else: 
#                         tmp_lst = map_lst
#                         break

#     # else해서 놓을 수 있는 자리가 아니었다면 다시 0으로 바꿔줘요

# print(map_lst)