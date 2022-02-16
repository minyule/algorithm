import sys
sys.stdin = open("input.txt")

lst = []
quest_num = int(input())
for _ in range(100):
    one = list(input())
    lst.append(one)
    # 2차원으로 입력받기

    # mid_x = 0
    # mid_y = 0
    # 시작 위치 0,0


    nx = 0
    ny = 0
    # 2차원 모든 항목에 대해 실행
    for mid_y in range(100):
        for mid_x in range(100):
            col_max = 1
            row_max = 1
            # 세로, 가로 길이 최댓값 초기화 ( 회문이 없으면 단어 하나짜리게 최대길이가 되므로 1)

            col_len = 0
            row_len = 0




            for comp_ud in range(1, 100):
                # 위아래 같은지 봄
                new_y_up = mid_y - comp_ud
                new_y_down = mid_y + comp_ud
                

                if 0 <= new_y_up < 100 and 0 <= new_y_down < 100: # 인덱스 에러 방지
                    if lst[new_y_up][mid_x] == lst[new_y_down][mid_x]:
                        # 상측, 하측 문자가 같으면
                        col_len = col_len + 2
                    else: # 상측, 하측 문자가 다르면
                        break
                    print(0, new_y_up, new_y_down)
                else: # 인덱스가 범위 넘어가면 멈춤
                    break
                

            for comp_rl in range(1, 100):
                # 좌우 같은지 봄
                new_x_left = mid_x - comp_rl
                new_x_right = mid_x + comp_rl
                

                if 0 <= new_x_left < 100 and 0 <= new_x_right < 100: # 인덱스 에러 방지
                    if lst[mid_y][mid_x - comp_rl] == lst[mid_y][mid_x + comp_rl]:
                        # 좌측, 우측 문자가 같으면
                        row_len = row_len + 2
                    else: # 좌측, 우측 문자가 다르면
                        break
                    print(1, new_x_left, new_x_right)
                else: # 인덱스가 범위 넘어가면 멈춤
                    break
            


print(col_max, row_max)