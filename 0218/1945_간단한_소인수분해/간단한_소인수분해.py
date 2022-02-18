import sys
sys.stdin = open("input.txt")

quest = int(input())

prime_num = [2, 3, 5, 7, 11] # 솟수 리스트

for quest_num in range(quest):
    prime_cnt = [0] * 5 # 솟수 횟수 리스트

    
    input_num = int(input())

    for idx in range(5):
        remainder = input_num % prime_num[idx] # 나머지가 0이 되어야 반복문 입장 가능 (반복문 입장용)
        while remainder == 0: # 나머지가 0이면 계속 반복. 0이 아니게되면 탈출
            input_num = input_num // prime_num[idx] # 몫
            prime_cnt[idx] = prime_cnt[idx] + 1
            remainder = input_num % prime_num[idx] # 나머지 (반복문 돌리는 용도)

    print(f'#{quest_num + 1} {prime_cnt[0]} {prime_cnt[1]} {prime_cnt[2]} {prime_cnt[3]} {prime_cnt[4]}')
