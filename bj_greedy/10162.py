# 전자레인지 : 최소버튼 조작
t = int(input())
button = [300, 60, 10]
cnt = [0, 0, 0]

for i in range(3):
  if t >= button[i]:
    cnt[i] += (t // button[i])
    t -= button[i] * cnt[i]

if t == 0:
  for x in cnt:
    print(x)
else:
  print(-1)
