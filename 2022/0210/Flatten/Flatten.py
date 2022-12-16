
import sys
sys.stdin = open("input.txt")

def max(lst):
    i_max = lst[0]
    for tmp in lst:
       if tmp > i_max:
           i_max = tmp
    return i_max

def min(lst):
    i_min = lst[0]
    for tmp in lst:
       if tmp < i_min:
           i_min = tmp
    return i_min

qust_num = 1
for _ in range(10):
    dump_num = int(input())
    box_heights = list(map(int, input().split()))

    # 덤프 횟수 dump_num 만큼 반복함
    for tries in range(dump_num):
        # 최대값 최소값 차이가 1 이하인 경우 break
        if max(box_heights) - min(box_heights) <= 1:
            break

        box_heights[box_heights.index(max(box_heights))] = max(box_heights) - 1
        box_heights[box_heights.index(min(box_heights))] = min(box_heights) + 1

    print(f'#{qust_num} {max(box_heights) - min(box_heights)}')
    qust_num += 1





    # print(dump_num, box_heights)

    # 큰 순서대로 나열

    # idx_max = 0
    # idx_min = -1

    #     if box_heights[idx_max] < box_heights[idx_max + 1]:
    #         idx_max += 1
    #     if box_heights[idx_min] > box_heights[idx_min - 1]:
    #         idx_min -= 1
    #
    #
    #
    #     if box_heights[idx_max] - box_heights[idx_min] <= 1:
    #         break
    # print(box_heights[idx_max] - box_heights[idx_min])

