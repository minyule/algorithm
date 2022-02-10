import sys
sys.stdin = open("sample_input(2).txt")

qust = int(input())

for qust_num in range(qust):
    k, n, m = map(int, input().split())
    charge_num = list(map(int, input().split()))
    charge_try = 0

    bus_location = 0
    bus_location_tmp = -1

    while bus_location < n:
        bus_location_tmp = -1
        # charge_num[c_num] 으로 정류장을 뒤에서부터 확인함
        for c_num in range(-1, -len(charge_num) - 1, -1):

            # 버스 이동한 거리 사이에 충전소 있으면 해당 충전소 위치가 버스 위치가 됨.
            if bus_location < charge_num[c_num] <= (bus_location + k):
                bus_location_tmp = bus_location
                bus_location = charge_num[c_num]
                charge_try += 1

                # 다음 횟수에서 도착 위치에 도착하게 된다면 이동거리 더하고 break
                if bus_location + k >= n:
                    bus_location += k
                    break

        # 정류장에 도착하지 못한 경우( bus_location_tmp가 -1임)
        if bus_location_tmp == -1:
            bus_location = 0
        # 모든 충전소를 보았을때, 지나친게 없으면( 그대로 초기값 0 이면)
        if bus_location == 0:
            charge_try = 0
            break

    print(f'#{qust_num + 1} {charge_try}')
