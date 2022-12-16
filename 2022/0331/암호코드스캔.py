from pprint import pprint
import sys
sys.stdin = open("암호코드스캔.txt")
# 2차원 배열을 입력받는다. 그 안에 암호코드가 들어있고, 아닌 부분은 0으로 이루어진 것 같다.
# 암호코드는 8개의 숫자로 구성되어있고, 각 숫자는 최소 7개의 숫자로 구성되어있다.
# 0과 1의 비율을 보고 숫자로 판단한다.#

dic = {
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15
}
# decoding = [[2, 1, 1], 
#             [2, 2, 1], 
#             [1, 2, 2],
#             [4, 1, 1],
#             [1, 3, 2],
#             [2, 3, 1],
#             [1, 1, 4],
#             [3, 1, 2],
#             [2, 1, 3],
#             [1, 1, 2]]

decoding = [[1, 1, 2], 
            [1, 2, 2], 
            [2, 2, 1],
            [1, 1, 4],
            [2, 3, 1],
            [1, 3, 2],
            [4, 1, 1],
            [2, 1, 3],
            [3, 1, 2],
            [2, 1, 1]]

testcase = int(input())

for test_num in range(1, 5):

    height, width = map(int, input().split())

    barcode_lsts = set()
    for _ in range(height):
        one_line = input()
    
        for one in one_line:
            if one != "0": # 0이 아닌게 있으면 바코드 있는 부분
                barcode_lsts.add(one_line)
                break

    print(barcode_lsts)


    barcode_lsts = list(barcode_lsts)


    for barcode_lst in barcode_lsts:






        ###### 바코드 행마다 같은 모양인지 확인하는 과정 필요 한가?

        # 16진수를 2진수로 바꾸기

        bin_barcode = ""
        for i in barcode_lst:
            if i.isdecimal():
                tmp = i
            else:
                tmp = dic[i]
            tmp = int(tmp)
            
            bin_num = ""
            for _ in range(4): # 2진수로 변환하는 과정
                bin_num = str(tmp % 2) + bin_num
                tmp = tmp // 2
            bin_barcode = bin_barcode + bin_num
        print(bin_barcode)
        # bin_barcode에는 바코드가 있는 행을 모두 2진수로 바꿔버린 값이 있음.
        # print(bin_barcode)

        bin_barcode = "0" + bin_barcode.strip("0") + "0"
        print(bin_barcode)

        # 비율에 맞게, 규칙에 맞게 십진수로 바꾸기

        # 뒤에서부터 확인.
        # 숫자가 변하는 순간, 축척된 값을 ratio에 넣어줌
        # bin_barcode = "0000011101101100010111011011000101100010001101001001101110110000"
        before_num = "0"
        accum = 0 # 0 또는 1이 연속으로 몇 번 반복했는지 확인하는 용도

        r_idx = 1
        ratio = []
        for bin_num in bin_barcode:
            # print(bin_num)

            if before_num != bin_num: # 다르면
                accum += 1
                ratio.append(accum)
                accum = 0 
                r_idx += 1
            else:
                accum += 1
            # r_idx += 1
            before_num = bin_num

        ratio = ratio[::-1]
        ratio.pop()
        print(ratio)
        # ratio = [1, 1, 4, 1, 2, 3, 1, 1, 2, 2, 1, 2, 3, 1, 2, 1, 3, 1, 2, 1, 2, 3, 1, 1, 2, 1, 1, 3, 1, 1, 2]

        deci_num = []
        for i in range(0, len(ratio), 4):
            # 최대공약수로 비율 최적화하기
            rat = ratio[i:i+3]

            # while rat not in decoding: # decoding에 없으면 비율 계산 할 필요가 있음.
            for _ in range(5):

                min = 10 # 일단 이 비율의 최소값을 구한다.
                for r in rat:
                    if r < min:
                        min = r
                # print(min)
                for sub in range(min, 1, -1):# r부터 2까지로 모든 값을 나눠보고 모든 경우에 대해 나머지가 없으면 그 떄의 값을 리스트에 저장함. 
                    tmp = [rat[0]%sub, rat[1]%sub, rat[2]%sub]
                    if tmp[0] == 0 and tmp[1] == 0 and tmp[2] == 0:
                        rat = [rat[0]//sub, rat[1]//sub, rat[2]//sub]
                        break

                    # print(tmp)

            print(rat)


            deci_num.append(decoding.index(rat))
            # print(decoding.index(ratio[i:i+3]))
            # continue
        deci_num = deci_num[::-1]
        print(deci_num)

        #? 어차피 3개씩 볼 꺼면 뒤에서부터 말고 앞에서부터 봐도 되지 않나? 101 비율만 볼꺼면

        # # 십진수 유효성 파악
        ans = 0
        for num in deci_num:
            ans = ans + num

        if (ans + (deci_num[0] + deci_num[2] + deci_num[4] + deci_num[6]) * 2) % 10: # 나머지가 있음: 10의 배수가 아님.
            numbers = 0
        else:
            numbers = ans
        print(test_num, numbers)



