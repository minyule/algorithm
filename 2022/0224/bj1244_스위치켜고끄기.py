import sys
sys.stdin = open("input.txt")

# switch_cnt_input = int(input()) # <=100 양의 정수 스위치 수

# switch_status = list(map(int, input().split())) # 스위치 상태. 1은 켜짐, 0은 꺼짐

# student_cnt_input = int(input()) # 학생 수 <= 양의 정수

# # print(switch_status) # 입력 확인

# # def change(lst, idx): # 스위치 바꾸는 함수를 만들었워요
# #     lst[idx] = int(not(lst[idx]))
# #     return lst

# for _ in range(student_cnt_input):

#     gender, switch_num = map(int, input().split()) # 남학생은 1, 여학생은 2



# # 남자인 경우
#     if gender == 1:
#         for boy_on_off in range(switch_num-1, switch_cnt_input, switch_num):
#             # change(switch_status, boy_on_off)
#             if switch_status[boy_on_off] == 0:
#                 switch_status[boy_on_off] = 1
#             else:
#                 switch_status[boy_on_off] = 0
#             # switch_status[boy_on_off] = not switch_status[boy_on_off]

# # 여자인 경우
#     else:
#         # 일단 받은 스위치는 바꿈
        
#         switch_num = switch_num - 1
#         switch_status[switch_num] = int(not(switch_status[switch_num]))
#         # change(switch_status, switch_num)

#         compare = switch_num 

#         # 비교를 반복할 횟수 정하기
#         if switch_cnt_input - switch_num <= switch_num -1:
#             compare = switch_cnt_input - switch_num

#         # if switch_cnt_input - switch_num > switch_num -1:
#         #     compare = switch_num 
#         # else:
#         #     compare = switch_cnt_input - switch_num

#         # print(switch_num, compare)

#         for pm in range(1, compare+1):
#             # # 양쪽이 같다면
#             # print(pm, switch_num - pm, switch_num + pm,
#             # switch_status[switch_num - pm] ,switch_status[switch_num + pm])
           
#             if switch_status[switch_num - pm] == switch_status[switch_num + pm]:
#                 switch_status[switch_num - pm] = int(not(switch_status[switch_num - pm]))
#                 switch_status[switch_num + pm] = int(not(switch_status[switch_num + pm]))
#                 # change(switch_status, switch_num - pm)
#                 # change(switch_status, switch_num + pm)
#             else: # 양쪽 다른 순간 끗
#                 break

# print(*switch_status)

# a=0
# print(int(not a))



# #------------교수님 풀이 메모메모
# n = int(input())

# switch = [-1] + list(map(int, input().split()))

# num_student = int(input())

# for _ in range(num_student):
#     gender, num = map(int, input().split())

#     # 남자일때
#     if gender == 1:
#         for i in range(num, n+1):
#             if i % num == 0:
#                 if switch[i] == 0:
#                     switch[i] =1
#                 elif switch[i] == 1:
#                     switch[i] =0


#     # 여자일때
#     elif gender ==2:
#         switch[num] = not switch[num]
#         k = 1
#         while 1:
#             if num - k >= 1 and num + k <= n:
#                 if switch[num-k] == switch[num +k]:
#                     switch[num-k] = not switch[num-k]
#                     switch[num+k] = not switch[num+k]
#                 else:
#                     break
#             else:
#                 break
#             k = k +1
# switch = list(map(int, input()))
# print(switch)

#-------------------------------- 교수님 코드
# n = int(input()) # <= 100

# switch = list(map(int,input().split())) # 스위치
# n = len(switch)
# # 인덱스와 번호를 일치시키기, 0, 1을 안쓰는 이유는 여성일 경우를 따로 처리해줘야해서
# switch = [-1] + switch

# num_student = int(input())

# # student = [list(map(int,input().split())) for _ in range(num_student)]

# def func(i):
#     if switch[i] == 0:
#         switch[i] = 1
#     elif switch[i] == 1:
#         switch[i] = 0



# for _ in range(num_student):
#     gender, num = map(int,input().split())

#     #남자일때는 ~~~
#     if gender == 1:
#         for i in range(num,n+1):
#             if i % num == 0:
#                 func(i)
#         # print(switch, '남자 다음 스위치')

#     #여자일때는~~
#     elif gender == 2:
#         # num 기준으로 대칭인 아이들의 상태를 바꾸겠어
#         switch[num] = not switch[num]
#         k = 1
#         while 1:
#             if num - k >= 1 and num + k <= n:
#                 if switch[num - k] == switch[num + k]:
#                     switch[num - k] = not switch[num - k]
#                     switch[num + k] = not switch[num + k]
#                 else:
#                     break
#             else:
#                 break
#             k += 1
#         #     print(switch, num,  k, "여자 while 안쪽")
#         # print(switch, '여자 다음 스위치')

# switch = list(map(int,switch))
# print(*switch[1:])





switch_cnt_input = int(input()) # <=100 양의 정수 스위치 수

switch_status = list(map(int, input().split())) # 스위치 상태. 1은 켜짐, 0은 꺼짐

student_cnt_input = int(input()) # 학생 수 <= 양의 정수

# print(switch_status) # 입력 확인

for _ in range(student_cnt_input):

    gender, switch_num = map(int, input().split()) # 남학생은 1, 여학생은 2



# 남자인 경우
    if gender == 1:
        for boy_on_off in range(switch_num-1, switch_cnt_input, switch_num):
            if switch_status[boy_on_off] == 0:
                switch_status[boy_on_off] = 1
            else:
                switch_status[boy_on_off] = 0

# 여자인 경우
    else:
        # 일단 받은 스위치는 바꿈
        switch_num = switch_num - 1
        switch_status[switch_num] = int(not(switch_status[switch_num]))

        # compare = switch_num 

        # 비교를 반복할 횟수 정하기
        # if switch_cnt_input - switch_num <= switch_num -1:
        #     compare = switch_cnt_input - switch_num +1

        # for pm in range(1, compare+1):
        #     # # 양쪽이 같다면
        #     if switch_status[switch_num - pm] == switch_status[switch_num + pm]:
        #         switch_status[switch_num - pm] = int(not(switch_status[switch_num - pm]))
        #         switch_status[switch_num + pm] = int(not(switch_status[switch_num + pm]))
        #     else: # 양쪽 다른 순간 끗
        #         break


        for pm in range(1, len(switch_status)):
            if 0 <= switch_num - pm < len(switch_status) and 0 <= switch_num + pm < len(switch_status):
            # # 양쪽이 같다면
                if switch_status[switch_num - pm] == switch_status[switch_num + pm]:
                    switch_status[switch_num - pm] = int(not(switch_status[switch_num - pm]))
                    switch_status[switch_num + pm] = int(not(switch_status[switch_num + pm]))
                else: # 양쪽 다른 순간 끗
                    break
            else:
                break
switch_status = [9] + switch_status

for i in range(1, len(switch_status)):
    print(switch_status[i], end=" ")
    if i%20 == 0:
        print()