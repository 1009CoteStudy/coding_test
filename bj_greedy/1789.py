# 수들의 합
s = int(input())

num = 1
cnt = 0
while s>=0:
    s -= num
    num += 1
    cnt += 1

print(cnt-1)
