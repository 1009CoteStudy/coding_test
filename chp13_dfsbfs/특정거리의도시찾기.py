# 모든 도로의 길이 = 1 => bfs
from collections import deque

# 입력값 : 도시, 도로, 거리, 출발도시번호
n,m,k,x = map(int, input().split())

# 모든 도시와 인접한 도시의 정보가 들어갈 그래프
graph = [[] for _ in range(n+1)] # 인덱스 0 비워놓기

# 모든 도로 정보 입력 받기
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)  # a 도시와 인접한 도시 b

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리 = 0

# BFS
q = deque([x])
while q:
    now = q.popleft() # 큐에서 현재 도시 꺼내기
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_city in graph[now]:
        # 방문하지 않은 도시라면
        if distance[next_city] == -1:
            distance[next_city] = distance[now] + 1
            q.append(next_city) # 큐에 삽입

# 최단거리가 k인 도시
check = False  ## 최단거리 체크를 위한 변수
for i in range(n+1):
    if distance[i]==k:
        print(i)
        check=True

# 최단거리가 k인 도시가 없는 경우
if check == False: print(-1)