import sys
sys.stdin = open("sample_input.txt")

quest = int(input())




for quest_num in range(quest):
    color = int(input())

    set_red = set()
    set_blue = set()
    set_purple = set()

    for _ in range(color):
        
        lst = list(map(int, input().split()))

        if lst[4] == 1: # red
            for i in range(lst[0], lst[2]+1):
                for j in range(lst[1], lst[3]+1):
                    set_red.add((i, j))
        if lst[4] == 2: # blue
            for i in range(lst[0], lst[2]+1):
                for j in range(lst[1], lst[3]+1):
                    set_blue.add((i, j))
        



        # print(set_red)
        # print(set_blue)

    # for red in set_red:
    #     if red in set_blue:
    #         set_purple.add(red)
    #         print(red)
    print(f'#{quest_num + 1} {len(list(set_red & set_blue))}')

