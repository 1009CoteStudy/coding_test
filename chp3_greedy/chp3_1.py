# 거스름돈
n = 1260
cnt = 0

coins = [500, 100, 50, 10]

for x in coins:
    cnt += n // x
    n = n % x

print(cnt)
