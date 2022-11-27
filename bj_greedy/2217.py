### 로프
n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=False)  # 오름차순
weight = []
for i in range(n):
    weight.append(rope[i]* (n - i))

print(max(weight))
