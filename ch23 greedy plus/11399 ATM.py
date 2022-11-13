n = int(input())

times = list(map(int, input().split()))
times.sort()

result = 0

for i in range(len(times)):
    result += times[i]*(n-i)

print(result)