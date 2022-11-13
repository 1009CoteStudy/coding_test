n, k = map(int, input().split())
coinTypes = []
for i in range(n):
    coinTypes.append(int(input()))

coinTypes.sort(reverse=True)

count = 0

for coin in coinTypes:
    if k>=coin:
        count += k//coin
        k= k%coin
    else:
        continue

print(count)