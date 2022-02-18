import sys
sys.stdin = open("sample_input.txt")

quest = int(input())

for quest_num in range(quest):
    lst = []
    max_len = 0
    for _ in range(5):
        one = input()
        lst.append(one)

        tmp_len = len(one)
        if tmp_len > max_len:
            max_len = tmp_len
    # 리스트로 입력받고, 단어의 최대 길이를 구함

    for idx in range(len(lst)):
        for _ in range(max_len - len(lst[idx])):
            lst[idx] = lst[idx] + ' '
    # 최대 길이보다 짧은 단어는 그 차이만큼 띄어쓰기를 뒤에 추가해줌

    ans = ''
    for word_idx in range(max_len):
        for word in lst:
            if word[word_idx] != ' ':
                ans = ans + word[word_idx]
    # 띄어쓰기 부분 없앰
    
    print(f'#{quest_num + 1} {ans}')
