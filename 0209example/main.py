# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# bubble_sort
def bubble_sort(num):
    for i in range(len(num) - 1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num
num = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(bubble_sort(num))

def counting_sort(input_arr, k):
    counting_arr = [0] * (k+1) #idx는 0부터 시자하므로 +1

    # COUNTS 숫자 세서 개수로 이루어진 리스트 만듦
    for i in range(0, len(input_arr)):
        counting_arr[input_arr[i]] += 1
    # 다른 방법
    for i in input_arr:
        counting_arr[i] +=1
    
    # 누적한 숫자 갖는 리스트 만듦
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i-1]

    # 오류 감지용. 정답은 0부터 있으므로 절대 나올 수 없는 -1로 디폴트 값을 넣어줌
    result_arr = [-1] * len(input_arr)

    # 숫자 후보 자리대로 만듦
    for i in range(len(result_arr) -1, -1, -1):
        counting_arr[input_arr[i]] -= 1
        result_arr[counting_arr[input_arr[i]]] = input_arr[i]

    #또는 뒤집고 진행
    input_arr = input_arr[::1-]
    for i in input_arr:
        counting_arr[i] -= 1
        result_arr[counting_arr[i]] =i

    return result_arr