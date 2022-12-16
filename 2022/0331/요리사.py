import sys
sys.stdin = open("요리사.txt")

testcase = int(input())
# N개의 식재료가 있음. (짝수개)
# 두 식재료를 합쳐서 한 요리 만듦
# 두 요리를 만들고,
# 맛의 차이가 최소가 되는 경우 그 최솟값

for test_num in range(1, 5):

    ingredient_cnt = int(input())

    table = []

    for _ in range(ingredient_cnt):
        one_line = list(map(int, input().split()))
        table.append(one_line)

    # 1부터 2~4, 2부터 3~4 ... 이렇게 

    plus_synergy = []
    minus_synergy = []
    for _ in range(ingredient_cnt * (ingredient_cnt - 1) // 2):
        minus_synergy.append([])
    # idx 번 재료에서 발생할 마이너스 값
    print(minus_synergy[1])

    i = 0
    for first_in in range(ingredient_cnt):
        for second_in in range(first_in + 1, ingredient_cnt):
            synergy_one = table[first_in][second_in] + table[second_in][first_in]
            plus_synergy.append(synergy_one)
            # first랑 second가 아닌 재료로 나오는 synergy를
            for thrid_in in range(ingredient_cnt):
                if thrid_in != first_in and thrid_in != second_in:
                    for fourth_in in range(thrid_in + 1, ingredient_cnt):
                        if fourth_in != first_in and fourth_in != second_in:
                            synergy_two = table[thrid_in][fourth_in] + table[fourth_in][thrid_in]
                            minus_synergy[i].append(synergy_two)
            i += 1
    # print(plus_synergy)   
            print(plus_synergy, minus_synergy)
            # print(first_in, second_in, table[first_in][second_in],table[second_in][first_in], synergy_one)

    ans = abs(plus_synergy[0] - minus_synergy[0][0])

    for plus_idx in range(len(plus_synergy)):
        for minus_idx in range(len(minus_synergy[plus_idx])):
            tmp = abs(plus_synergy[plus_idx] - minus_synergy[plus_idx][minus_idx])
            if ans > tmp:
                ans_pl = plus_synergy[plus_idx]
                ans_mi = minus_synergy[plus_idx][minus_idx]
                ans_pli = plus_idx
                ans_mii = minus_idx
                ans = tmp

    print(ans, ans_pl, ans_mi, ans_pli, ans_mii)