n = int(input())

times = []
for i in range(n):
    times.append(list(map(int, input().split())))

count = 0
finishTime = 0

for j in range(len(times)):
    if finishTime<times[i][0]:
       count += 1
       finishTime = times[i][1]
