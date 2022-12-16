from pprint import pprint
import sys
sys.stdin = open("단순2진암호코드.txt")

# 8개의 숫자로 이루어짐
# 앞 7개 숫자는 상품 고유의 번호를 나타내고, 마지막 자리는 검증코드
# 검증코드 계산 방법:
# 홀수 자리 합 * 2 + 짝수자리합 + 검증코드 가 10의 배수가 되어야함.
# 
# 세로 50, 가로 100 이하의 직사각형 배열에 암호코드정보 전달.
# 하나의 배열에 1개의 암호코드 존재
# 정상 암호코드인지 확인하고, 
# 이 암호코드들에 적혀있는 숫자들의 합 출력
# 
# 모든 암호토드는 8개의 숫자로 구성, 세로 길이는 5~ 50칸# =====


# 2차원으로 배열이 주어지는데, 그 사이에 바코드가 있음. 바코드가 아닌 부분은 0임
# 바코드를 규칙에 맞게 숫자로 바꾸면 암호코드가 되는데, 암호코드를 해석해야함.
# 암호코드는 8개의 숫자로 이루어져있음
# 마지막 숫자를 제외하고, 홀수자리숫자합 *3 +짝수자리숫자합 에 마지막숫자를 더해서 10의 배수가 되면
# 올바른 암호코드임.
# 올바른 암호코드면 그 바코드의 모든 숫자 합을 출력하고, 그렇지 않으면 0출력#

decoding = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]


testcase = int(input())

for test_num in range(1, testcase + 1):

    N, M = map(int, input().split()) # N은 배열의 세로 크기, M은 배열의 가로 크기

    # 1. 뒤에서부터 확인했을 때, 1이 나오면 바코드의 끝 부분#
    base = []
    barcodes = ""
    numbers = ""
    for i in range(N):
        one_line = input()
        base.append(one_line)
        # if "1" in one_line: # 입력 받은 줄에 1이 있으면 바코드가 있는 부분
        for idx in range(-1, -M-1, -1): # 뒤에서부터 확인했을 때, 
            if one_line[idx] == "1": # 1이 처음 나오는 곳이 바코드의 끝부분
                if not numbers:
                    barcodes = one_line
                    for i in range(idx, idx-50, -7):
                        new_numbers = numbers

                        for decode in range(10):
                            if one_line[i-6:i+1] == decoding[decode]:
                                new_numbers = str(decode) + new_numbers
                        
                        if new_numbers == numbers: # 아무것도 추가된 것이 없으면
                            numbers = 0
                            break
                        else: # 추가된 게 있으면 갱신
                            numbers = new_numbers
                    break
                
                elif one_line != barcodes:
                    numbers = 0
                    break

    # 암호코드 유효성 검사

    if numbers: # 바코드는 잘 나옴
        numbers = list(map(int, numbers))
        ans = 0
        for idx in range(8): # 총 합 구하고
            ans = ans + numbers[idx]
        # 10으로 나눈게 0이 아니면 유효하지 않음
        if (ans + (numbers[0] + numbers[2] + numbers[4] + numbers[6]) * 2) % 10:
            numbers = 0
        else:
            numbers = ans
    print(f'#{test_num} {numbers}')












            
            # if one_line[idx] == "1" and (not numbers): # 1이고 numbers 비어있으면 바코드 첫 줄임
            #     # 0, 1이 바뀌는 것을 측정해서 바로 numbers에 넣어줄게요.




            #     barcodes.append(one_line[idx-55:idx+1]) # 바코드 길이(56) 만큼 barcode에 잘라냄
            #     break



# pprint(barcodes)
# pprint(base)

# # 2. barcode를 뒤에서부터 7개씩 끊어서 숫자로 바꿈
# barcode = barcodes[0]
# # numbers = ""

# for bar in range(0, 56, 7):
    

# 마지막에 모든 바코드의 행이 같은 숫자를 가리키는지 확인하기




