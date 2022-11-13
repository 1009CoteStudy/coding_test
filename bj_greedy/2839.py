## 설탕 배달
n = int(input())  # 18
cnt = 0

while (1):
  if (n % 5) == 0:  # 큰 수의 배수인지 먼저 확인
    cnt += n // 5
    break
  n -= 3
  cnt += 1

if n < 0:
  cnt = -1
print(cnt)
