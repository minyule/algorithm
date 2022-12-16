import sys
sys.stdin = open("중위순회_input.txt")

for test_num in range(1, 11):
    
    node = int(input())

    tree = []
    for _ in range(node + 1):
        tree.append([0, 0])

    tree = [None]
    for _ in range(node):
        one_line = list(input().split())
        tree.append(one_line[1])


    ans = ""

    now = 1
    while now *2 <= node:
        now = now * 2

    visited = []

    for _ in range(node):

        visited.append(now)

        ans = ans + tree[now] # 현재 글자 추가

        if now * 2 >= node or (now * 2 in visited and now * 2 + 1 in visited): # 자식이 없거나 모두 방문 끝이면
            while now in visited: # 현재 위치가 방문한 곳이면,
                now = now // 2



        elif now * 2 + 1 <= node: # 오른쪽자식 있으면
            
            now = now * 2 + 1 # 오른쪽 자식 위치로 가고,

            while now * 2 <= node: # 오른쪽 자식의 자식이 있으면
                now = now * 2 # 왼쪽 끝으로 감


        # 오른쪽 자식이 없고
        elif now % 2 == 0 : # 짝수면(왼쪽아이이면)
            now = now // 2 # 부모로 위치 이동

        # 오른쪽 자식 없고
        elif now % 2 == 1: # 홀수면(오른쪽아이이면)
            now = (now - 1) // 2
        # print(len(visited), now, ans)
    print(f'#{test_num} {ans}')


