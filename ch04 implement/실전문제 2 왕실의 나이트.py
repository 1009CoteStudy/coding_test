n = input()
x = ord(n[0]) - ord('a') + 1
y = int(n[1])

count = 0

xMove = [2, 2, -2, -2, 1, 1, -1, -1]
yMove = [1, -1, 1, -1, 2, -2, 2, -2]

for i in range(len(xMove)):
    nx = x + xMove[i]
    ny = y + yMove[i]
    if 1<=nx and nx<=8 and 1<=ny and ny<=8:
        count+=1

print(count)