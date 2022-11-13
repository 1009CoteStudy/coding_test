# 거스름돈 : 개수가 가장 적게
n = int(input())

cash = 1000 - n  # = 620
cnt = 0
coins = [500, 100, 50, 10, 5, 1]

for x in coins:
  if cash >= x:
    cnt += (cash // x)
    cash %= x

print(cnt)
