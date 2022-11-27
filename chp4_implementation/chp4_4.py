# 게임 개발

# 입력 받기
n,m = map(int,input().split())
x,y,dir = map(int,input().split())

gameMap = []
for i in range(n):
    gameMap.append(list(map(int, input().split())))

