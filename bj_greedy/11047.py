### 동전 0
n, k = map(int, input().split())

coin_list = list()
for i in range(n):
  coin_list.append(int(input()))

cnt = 0

for x in reversed(coin_list):  # 역방향
  if k >= x:  # 굳이 필요 없는 if문
    cnt += (k // x)
    k %= x
  if k == 0:
    break
print(cnt)
