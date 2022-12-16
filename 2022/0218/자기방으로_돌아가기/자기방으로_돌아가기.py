import sys
sys.stdin = open("sample_input.txt")

quest = int(input())

for quest_num in range(quest):

    students = int(input()) # 돌아가야할 학생들의 수

    lst = []

    rooms_lst = [0] * (201)

    for _ in range(students):
        # lst.append(list(map(int, input().split())))
        lst = list(map(int, input().split()))

        for i in range(2):
            if lst[i] % 2 == 1:
                lst[i] = lst[i] // 2 + 1
            else:
                lst[i] = lst[i] // 2


        print(lst)



    #     if lst[0] > lst[1]: ######## 큰호수에서 작은호수로 가는경우 생각 못했다. 순서 바꿔줌
    #         tmp = lst[1]
    #         lst[0] = tmp
    #         lst[1] = lst[0]




    # #     for ways in range(lst[0] - 1, lst[1] + 2):
    # #         rooms_lst[ways] = rooms_lst[ways] + 1


    # # max = 0
    # # for ways in rooms_lst:
    # #     if max < ways:
    # #         max = ways

    # print(f'#{quest_num + 1} {max}')






    # rooms_lst = [0] * 400

    # for _ in range(students):
    #     # lst.append(list(map(int, input().split())))
    #     lst = list(map(int, input().split()))

    #     for ways in range(lst[0], lst[1] + 1):
    #         rooms_lst[ways] = rooms_lst[ways] + 1


    # max = 0
    # for ways in rooms_lst:
    #     if max < ways:
    #         max = ways

    # print(f'#{quest_num + 1} {max}')

