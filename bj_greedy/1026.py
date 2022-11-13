n = int(input())

data_a = list(map(int, input().split( )))
data_b = list(map(int, input().split( )))

sorted_a = sorted(data_a, reverse=True)  # 내림차순

s = 0
for i in range(n):
  s += sorted_a[i] * min(data_b)
  data_b.pop(data_b.index(min(data_b)))

print(s)
