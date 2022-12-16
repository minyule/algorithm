import sys
sys.stdin = open("Contact.txt")

inp, start = map(int, input().split())

l_inp = list(map(int,input().split()))

student_lst = []
for _ in range(101):
    student_lst.append([])

for i in range(0, inp, 2):
    student_lst[l_inp[i]].append(l_inp[i+1])

# student_lst 에서 인덱스 번호에 있는 학생은
# 그 인덱스 위치의 리스트 안에 있는 학생들에게 연락 가능

visited = []
stack = []

now = start

visited.append(now)
stack.append(now) # stack 마지막에 있는 곳이 현재 위치


# 더 갈 곳이 없으면
if len(student_lst[now]) == 0: 
    now = stack.pop()


# 간 적 없는 애면 이동
if student_lst[now] not in visited:
    now = student_lst[now]
    visited.append(now)
    stack.append(now)

# 간적 있는 애들이면
else:
    now = stack.pop()


# if student_lst[now][-1] in visited:
#     now = stack.pop()


print(len(student_lst))