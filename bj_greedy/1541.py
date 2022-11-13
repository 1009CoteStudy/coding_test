### 잃어버린 괄호
sen = input().split('-')

numbers = []  # 뺄셈 진행할 숫자들

for x in sen:
    res = 0
    num = x.split('+')
    for y in num:
        res += int(y)  # 덧셈 계산
    numbers.append(res)

int_numbers = list(map(int, numbers))
first = int_numbers[0]
for i in range(len(int_numbers)-1):
    first -= int_numbers[i+1]

print(first)