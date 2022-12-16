from pprint import pprint
import sys
sys.stdin = open("최소이동거리.txt")

testcase = int(input())

N, E = map(int, input().split())

node_lst = [[] for _ in range(N + 1)] # 인덱스 0인 곳에는 0에서 갈 수 있는 노드가 들어갈 것
distance_lst = [[] for _ in range(N + 1)] # 거리

for _ in range(E):
    i, a, b = map(int, input().split())
    node_lst[i].append(a)
    distance_lst[i].append(b)

# 0에서 N까지 가는데에 걸리는 최소한의 거리
distance = 0

# 1. 스택 어쩌구 해서 쭉쭉 감. #
now = 0
end = N

stack = []
visited = [0 for _ in range(N+1)]

total_dis = 0
total_dis_lst = []

for to_node in node_lst[0]:
    stack.append(0)
    visited[0] = 1
    now = to_node
    while stack:
        if visited[now] == 0: # 방문한 적 없는 곳임.
            stack.append(now)
            visited[now] = 1 # 방문한 곳은 1로 바꿈
            total_dis = total_dis + distance_lst[now]

        elif visited[now] == 1: # 방문한 적 있음.
            stack.pop()
            total_dis = total_dis - distance_lst[now]

        if stack[-1] == end: # 도착지 도착하면 총 길이 저장해두고 0으로 초기화 now 초기화.. break
            






