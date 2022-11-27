n = int(input())
n_len = len(str(n))

ls = []
for _ in range(n_len):
    ls.append(n%10)
    n = n//10

right = 0
left=0
for i in range(n_len//2):
    right += ls[i]
    left += ls[i+n_len//2]

if right==left: print('LUCKY')
else: print('READY')