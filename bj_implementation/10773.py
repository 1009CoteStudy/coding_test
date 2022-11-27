# 제로
n = int(input())
numbers = []
for _ in range(n):
    x = int(input())
    if x != 0:
        numbers.append(x)
    else:
        numbers.pop(-1)

print(sum(numbers))