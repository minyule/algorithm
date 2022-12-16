import sys
sys.stdin = open("전기버스2.txt")

# 교체횟수 최소로. 최소 교체횟수 출력
# 마지막 정류장에는 배터리가 없음. 도착하면 끝
# 출발지의 배터리가 처음 배터리 양#
testcase = int(input())

for test_num in range(1, testcase + 1):

    battery = list(map(int, input().split())) # 인덱스 1부터 배터리용량

    N = battery[0] # 정류장 수
    battery = battery[1:] # 배터리 양  









































    # 정류장을 뒤에서부터 보면서
    # 도착지까지 거리 <= 배터리 양인 곳 중, 출발지에 가장 가까운 곳 찾을 것.
  
    # change_cnt = 0 # 배터리 교체 횟수

    # while state > 1:

    #     distance = 1
    #     for station in range(-1, -state, -1):
    #         if battery[station] >= distance:
    #             tmp_dis = distance
    #             print(station, distance)
                
    #         distance += 1
    #     state = state - tmp_dis
    #     if state <= 1:
    #         break
    #     change_cnt += 1
        


    #     print(test_num, tmp_dis, change_cnt, state)
    # # print(N, battery)