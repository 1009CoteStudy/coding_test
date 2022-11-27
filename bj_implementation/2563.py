### 색종이
n = int(input())

# 이차원 배열 생성
arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1

# arr가 1인 부분 = 넓이
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j]==1: cnt += 1

''' 다른 방식
for row in arr:
    cnt += row.count(1)  # 배열.count(a) : 배열의 값이 a인 칸의 수
'''
print(cnt)