import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []
visited = [ [False] * N for _ in range(N) ]

for i in range(N):
    graph.append(list(str(sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(cur, x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == '0' or visited[nx][ny]:
                continue

            if graph[nx][ny] == '1':
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = str(cur)
                cnt += 1

    return cnt

cur = 2
cnt = 0
answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            answer.append(bfs(cur, i, j))
            cur += 1
            cnt += 1

answer.sort()

print(cnt)

for data in answer:
    print(data)