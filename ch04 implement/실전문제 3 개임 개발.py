n, m = map(int, input().split())
x, y, head = map(int, input().split())

gameMap = []
for i in range(n):
    gameMap.append(list(map(int, input().split())))

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

gameMap[x][y] = 1

def turnLeft():
    global head
    head -= 1
    if head == -1:
        head = 3

turnCount = 0
moveCount = 0

while True:
    turnLeft()
    turnCount += 1
    if turnCount == 4:
        nx = x - direction[head][0]
        ny = y - direction[head][1]
        moveCount += 1
        if gameMap[nx][ny] == 1:
            break
    nx = x + direction[head][0]
    ny = y + direction[head][1]
    moveCount += 1
    if gameMap[nx][ny] == 1:
        continue

print(moveCount)