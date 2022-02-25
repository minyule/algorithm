import sys
sys.stdin = open("sample_input.txt")

testcase = int(input())

for test_num in range(1, testcase + 1):

    N, K = map(int, input().split())

    subjects = list(map(int, input().split()))

    top_K = [0] * K # 포함될 과목 점수 들어갈 리스트

    ans = 0

    for top_i in range(K): # K 번 반복

        for tmp_idx in range(len(subjects)): # 최대 과목 점수 찾아서 리스트에 넣기
            if top_K[top_i] < subjects[tmp_idx]:
                top_K[top_i] = subjects[tmp_idx]
                del_idx = tmp_idx # 없앨곳의 인덱스값 저장해놓음

        ans = ans + top_K[top_i]

        subjects.pop(del_idx)

    print(f'#{test_num} {ans}')