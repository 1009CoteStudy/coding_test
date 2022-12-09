import math

N = int(input())

flag = int(math.sqrt(N))

cnt = 0

for i in range(flag, 0, -1):
    if 