# 위에서 아래로
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

# 출력 : 숫자 사이 공백 포함
for x in array:
    print(x, end=' ')