from gettext import find
import sys
sys.stdin = open("test_input.txt", 'rt', encoding='UTF8')

quest = int(input())
# 보이어-무어 알고리즘 사용하기
find_str = input() # 찾을 문자열
long_str = input() # 여기에서 찾을거임.

base = 0 # long_str 옮길 거리
n = len(find_str) - 1 # 찾을 문자열의 길이. 길이를 인덱스로 사용할 것이므로 -1

while base <= len(long_str):
    if find_str[n] == long_str[base + n]: # 맨 끝부분이 같으면 
        for i in range(-2, -len(find_str) -1, -1): # 뒤에서부터 앞까지 비교
            if find_str[i] == long_str[base + i +1]: # 같으면
                
                


        print("fin")
    else: # 맨 끝부분이 다르면 base 키워서 long_str을 find_str 끝 글자에 맞춤
        while long_str[base + n] != find_str[n]:
            base = base + 1
            print(base)