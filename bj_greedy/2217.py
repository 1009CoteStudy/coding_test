# 로프
n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

ans = list(reversed(rope))[-1] * n
print(ans)

