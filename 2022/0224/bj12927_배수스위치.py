# 교수님 풀이 메모메모

from tkinter import N


lights = input()
# input()
# 1번 누르고 2번 누르는 것과 2번 누르고 1번 누르는 것은 같은 행위.

n = len(lights)

# idx랑 번호를 일치시키고 싶음.
lights = list("N" + lights) # 인덱스 0 자리에 더미데이터 하나를 넣어줌. 꺼진상태로.
# 값을 바꿀 필요가 있으니까 리스트로 만들어줌



cnt = 0 # 스위치 누른 횟수

for i in range(1, n+1): # 인덱스 주의
    # 스위치 누르는 과정 필요할듯.
    # 켜져있는 아이를 꺼야함

    if lights[i] == "Y": # 켜져있었으면 꺼야함
        cnt = cnt + 1
        num = i

        # 1. while 방법
        # while 1: #i의 배수에서 실행해야해
        #     if num <= n: # 반복문 
        #         if lights[num] == "N":
        #             lights[num] = "Y"
        #         elif lights[num] == "Y":
        #             lights[num] = "N"
        #         num += i
        #     else:
        #         break
        # while num <= n: #i의 배수에서 실행해야해
        #     if lights[num] == "N":
        #         lights[num] = "Y"
        #     elif lights[num] == "Y":
        #         lights[num] = "N"
        #         num += i
        #     else:
        #         break

        # 2. 나머지 방법
        # i로 나눈 나머지가 0일때 진행
        # for j in range(i, n+1, i):
        for j in range(i, n+1, i):
            # if j % i == 0:
            if lights[j] == "N":
                lights[j] = "Y"
            elif lights[j] == "Y":
                lights[j] = "N"
        # print(lights)


print(cnt)
