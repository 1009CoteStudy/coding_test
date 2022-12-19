# 미해결
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

visited = [False] * (N + 1)
graph = [ [] for _ in range(N + 1) ]

for i in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    x, y = min(x, y), max(x, y)

    graph[x].append(y)

def bfs(start):    
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in range(len(graph[v])):
            if not visited[graph[v][i]]:
                queue.append(graph[v][i])
                visited[graph[v][i]] = True

cnt = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)