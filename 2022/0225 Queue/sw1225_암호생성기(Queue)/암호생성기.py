
import sys
sys.stdin = open("input.txt")

for _ in range(10):


    test_num = int(input())

    num_lst = list(map(int, input().split()))

    rear = -1
    front = -1

    minus = 1
    stop = 0
    while stop == 0:
        minus = 1
        for _ in range(5):

            num_lst.append(num_lst[0] - minus) # 뒤에 넣고
            num_lst.pop(0) # 앞에선 뺌

            if num_lst[-1] <= 0: # 마지막꺼가 0 이하면 끗
                num_lst[-1] = 0
                stop = 1
                break

            minus = minus + 1


    print(f"#{test_num}", end=" ")
    print(*num_lst)


