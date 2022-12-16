# # This is a sample Python script.

# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# lst = [list(map(int, input().split())) for _ in range(20)]
# num_apt = 1
# for numQ in range(0, 19, 2):
#     total = 0
#     # lst[numQ + 1]은 문제별 아파트들 리스트
#     for one_apt in range(2, len(lst[numQ + 1]) - 2):
#
#         # lst[numQ+1][one_apt] 는 각 아파트 하나의 높이 ex 225
#         tmp_compare = 300
#         # 양쪽 4개의 아파트와 층고 차이 중 제일 작은 값 ( 겹치지 않는 부분)
#         for compare_4 in [-2, -1, 1, 2]:
#             dif_4 = lst[numQ + 1][one_apt] - lst[numQ + 1][one_apt + compare_4]  # 층수 차이
#             if dif_4 > 0:  # 층수차이가 양수면 ( 기준 아파트가 제일 큼)
#                 if dif_4 < tmp_compare:  # 이전 층수 차이보다 작으면 (tmp를 가장 작은 값으로 만듦)
#                     tmp_compare = dif_4
#             else:  # 층수차이가 음수거나 0이면 ( 기준아파트가 완전히 가려짐)
#                 tmp_compare = 0
#         total = total + tmp_compare  # 층수차이들을 total에 모두 더함
#
#     print("#{0} {1}".format(num_apt, total))
#     num_apt += 1


import sys
sys.stdin = open("input.txt")
lst = []

for _ in range(20):
    # lst = [list(map(int, sys.stdin.readline().split())) for _ in range(20)]
    a = sys.stdin.readline()
    lst_inp = list(map(int, a.split()))
    lst.append(lst_inp)
num_apt = 1
for numQ in range(0, 19, 2):
    total = 0
    # lst[numQ + 1]은 문제별 아파트들 리스트
    for one_apt in range(2, len(lst[numQ + 1]) - 2):

        # lst[numQ+1][one_apt] 는 각 아파트 하나의 높이 ex 225
        tmp_compare = 300
        # 양쪽 4개의 아파트와 층고 차이 중 제일 작은 값 ( 겹치지 않는 부분)
        for compare_4 in [-2, -1, 1, 2]:
            dif_4 = lst[numQ + 1][one_apt] - lst[numQ + 1][one_apt + compare_4]  # 층수 차이
            if dif_4 > 0:  # 층수차이가 양수면 ( 기준 아파트가 제일 큼)
                if dif_4 < tmp_compare:  # 이전 층수 차이보다 작으면 (tmp를 가장 작은 값으로 만듦)
                    tmp_compare = dif_4
            else:  # 층수차이가 음수거나 0이면 ( 기준아파트가 완전히 가려짐)
                tmp_compare = 0
        total = total + tmp_compare  # 층수차이들을 total에 모두 더함

    print("#{0} {1}".format(num_apt, total))
    num_apt += 1