import sys
sys.stdin = open("input.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    N, M = map(int, input().split()) # N은 A의 길이, M은 B의 길이

    # 무조건 B가 길거나 같도록 (A가 짧으니까 B의 인덱스를 이동하면서 계산해줄것임)
    if N < M:
        A_lst = list(map(int, input().split()))
        B_lst = list(map(int, input().split()))
    else:
        B_lst = list(map(int, input().split()))
        A_lst = list(map(int, input().split()))
        

    sum = 0
    # 겹쳐지는 부분의 합을 구함 -> 출력할 변수 초기화 해야해
    for idx in range(len(A_lst)):
        sum = sum + A_lst[idx] * B_lst[idx]
    ans = sum



    # 최대로 인덱스 차이가 나는 만큼은 각 len의 차이
    for move_idx in range(1, len(B_lst) - len(A_lst) + 1):
        sum = 0

        for idx in range(len(A_lst)): # B 인덱스 이동해가면서 곱의 합 구하기
            sum = sum + A_lst[idx] * B_lst[idx + move_idx]

        if ans < sum:
            ans = sum

    print(f'#{test_num} {ans}')