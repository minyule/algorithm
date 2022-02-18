from re import I
import sys
sys.stdin = open("sample_input.txt")

quest = int(input())

for quest_num in range(quest):
    all = "0" + input() + "0"

    total_iron = 0 # 답으로 나올 철근 수

    now_iron = 0 # 당장 레이저 조사시 쪼개질 철근 수

    long_iron = 0 # 온전한 철근 수

    # 1. ( 만 나오면 now_iron 추가, long_iron 추가
    # 2. ) 만 나오면 now_iron 빼기
    # 3. () 나오면 total_iron은 now_iron만큼 증가


    # print(all[1])


    for iron in range(1, len(all) - 1):

        # () 가 나오면 
        if all[iron] == "(" and all[iron + 1] == ")":
            # print("laser")
            total_iron = total_iron + now_iron

        elif all[iron - 1] == "(" and all[iron] == ")":
            continue
        
        # ( 만 나오면
        elif all[iron] == "(":
            now_iron = now_iron + 1
            long_iron = long_iron + 1

        # ) 만 나오면
        elif all[iron] == ")":
            now_iron = now_iron - 1
        
    total_iron = total_iron + long_iron

    print(f'#{quest_num + 1} {total_iron}')

# print(all)