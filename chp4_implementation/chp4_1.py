# 상하좌우
n = int(input())
plans = input().split()

# L, R, U, D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
moves = ['L', 'R', 'U', 'D']
# 현재위치
x,y = 1,1

for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    # 공간을 넘는 경우
    if nx<1 or ny<1:
        continue

    # 그렇지 않은 경우 이동
    x,y = nx, ny

print(x,y)