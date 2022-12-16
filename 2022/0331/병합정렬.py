import sys
sys.stdin = open("병합정렬.txt")

# merge sort

# 리스트를 나누기
def merge_sort(lst):
    global ans

    if len(lst) == 1: # 리스트의 길이가 최소 (1)가 되면 중단
        return lst 

    middle = len(lst) // 2 # 중간을 기준으로
    left = lst[:middle] # 왼쪽 리스트와
    right = lst[middle:] # 오른쪽 리스트


    
    # 각 리스트에 대해 분할을 해줌
    left = merge_sort(left)
    right = merge_sort(right)
     
    return merge(left, right)

# 병합하기
def merge(left, right):
    global ans
    result = []
    i = 0
    j = 0
    len_left = len(left)
    len_right = len(right)

    # if left and right:
    if left[-1] > right[-1]:
        ans = ans + 1
        # print(left, right)

    while i<len_left or j<len_right: # left, right중 하나라도 남아있으면
        

        if i<len_left and j<len_right: # 둘다 남아있는 경우,

            if left[i] <= right[j]: # left앞에 있는게 작아서 결과에 넣어줌
                result.append(left[i])
                i+=1
            else: # 오른쪽 것을 넣어줘야하는 경우
                result.append(right[j])
                j+=1
        else:
            if i<len_left: # 왼쪽만 남아있는 경우
                result.append(left[i]) # 다 결과에 붙여줌
                i +=1
            elif j<len_right:
                result.append(right[j])
                j +=1
    return result

# 왜 교수님 코드로 하면 무한루프 도는 일이 생길까?
# i, j로 해줘야지만 무한루프가 돌지 않는 이유가 궁금하다.#




testcase = int(input())

for test_num in range(1, testcase + 1):

    N = int(input())

    ans = 0

    lst = list(map(int, input().split()))

    ans_lst = merge_sort(lst)

    print(f"#{test_num} {ans_lst[len(ans_lst)//2]} {ans}")

