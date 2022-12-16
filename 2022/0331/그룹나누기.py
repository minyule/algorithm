import sys
sys.stdin = open("그룹나누기.txt")

testcase = int(input())
for test_num in range(1, testcase + 1):

    N, M = map(int, input().split()) # N명의 학생이 있고, M번의 짝꿍 요청이 있음.

    status = [0 for _ in range(N+1)] # 인덱스 번호의 학생이 몇 번 조에 들어갔는지 나타냄
    # group = [[] for _ in range(N+1)] # 어떤 학생이 이 그룹에 속해있는지 나타냄

    num_group = 0

    inp_lst = list(map(int, input().split()))
    for i in range(0, M*2, 2): # inp_lst[i]는 요청한 학생, inp_lst[i+1]는 요청받은 학생
        # 학생의 조 확인.
        # 신청한 학생은 조가 있고, 신청받은 학생이 조가 없으면
        # 신청한 학생은 조가 없고, 신청받은 학생이 조가 있으면
        # 신청한 학생과 신청받은 학생 모두 조가 없는 경우#

        # 신청한 학생과 신청받은 학생 모두 조가 없는 경우
        if status[inp_lst[i]] == 0 and status[inp_lst[i+1]] == 0:
            # 새로운 조를 만들어서 넣어줌.
            num_group = num_group + 1
            status[inp_lst[i]] = num_group
            # 요청받은 학생도 그 조에 넣어줌
            status[inp_lst[i+1]] = num_group

        # 신청한 학생이 조가 있는데 신청받은 학생이 조가 없으면
        elif status[inp_lst[i+1]] == 0 and status[inp_lst[i]] != 0:
            # 신청한 학생의 조에 넣어줌
            status[inp_lst[i+1]] = status[inp_lst[i]]

        # 신청한 학생은 조가 없고, 신청받은 학생이 조가 있으면
        elif status[inp_lst[i]] == 0 and status[inp_lst[i+1]] != 0:
            # 그 학생의 조에 요청받은 학생을 넣어줌
            status[inp_lst[i]] = status[inp_lst[i+1]]
        
        # 두 학생 모두 어딘가에 속해있는 경우,
        # 요청받은 애의 조에 속한 애들 전부를 요청한 애의 조에 넣어줄게요
        else:
            before = status[inp_lst[i+1]]
            to_group = status[inp_lst[i]]
            for addiction in range(N+1):
                if status[addiction] == before:
                    status[addiction] = to_group

    # 모든 요청을 처리한 후에
    # 아무런 조에 속하지 않은 친구는 순서대로 새로운 조를 만들어서 넣어줌
    for no_group in range(1, N+1):
        if status[no_group] == 0:
            num_group = num_group + 1
            status[no_group] = num_group

    # 중복된 조와 인덱스 0 제거 후 출력
    status = len(list(set(status)))-1
            
    print(f"#{test_num} {status}")