# 요세푸스 문제 0
n, k = map(int,input().split())

circle = [(x+1) for x in range(n)]
del_circle = []

cur = 0
for i in range(n):
    cur = (cur+k-1) % len(circle)
    next = circle.pop(cur)
    del_circle.append(next)

print('<', end="")
for i in range(n):
    if i == (n - 1):
        print(del_circle[i],end="")
        print('>')
        break
    print(del_circle[i],end=", ")
