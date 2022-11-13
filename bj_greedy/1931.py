# 회의실 배정
n = int(input())
time = []
for i in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

print(time)