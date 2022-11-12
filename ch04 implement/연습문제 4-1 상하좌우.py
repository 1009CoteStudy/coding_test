#연습문제 4-1 상하좌우

n = int(input())
plans = list(input().split())

x, y = 1, 1

moveTypes = ['L', 'R', 'U', 'D']
xMove = [0, 0, -1, 1]
yMove = [-1, 1, 0, 0]


for plan in plans:
    for i in range(len(moveTypes)):
        if plan == moveTypes[i]:
            nx = x+xMove[i]
            ny = y+yMove[i]
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x, y = nx, ny

print(x, y)