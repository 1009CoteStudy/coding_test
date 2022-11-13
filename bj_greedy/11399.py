# ATM 총 걸리는 시간
n = int(input())
time = list(map(int, input().split()))

min_ls = []
time_sum = 0
for i in range(n):
  min_ls.append(min(time))
  time_sum += sum(min_ls)
  time.remove(min(time))

print(time_sum)
