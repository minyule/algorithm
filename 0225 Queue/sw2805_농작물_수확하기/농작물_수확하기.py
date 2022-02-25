import sys
sys.stdin = open("input.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    N = int(input())



    harvests = 0

    start = N // 2
    end = N // 2 + 1


    for half_one in range(N // 2): # 가운데 제일 긴 줄 직전까지 받아

        lst = list(map(int, input())) # 입력 받을때 주의


        for h_idx in range(start, end):
            harvests = harvests + lst[h_idx]


        start = start - 1
        end = end + 1



    for half_two in range(N // 2, N): # 가운데 제일 긴 줄부터 마지막까지 받아

        lst = list(map(int, input()))

        for h_idx in range(start, end):
            harvests = harvests + lst[h_idx]

        start = start + 1
        end = end - 1

    print(f'#{test_num} {harvests}')