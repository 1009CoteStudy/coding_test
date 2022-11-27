key = []

for i in range(n):
	key.append(list(map(int, input().split())))

def rotate90(key):
    n = len(key)
    rotateKey = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            rotateKey[c][n-1-r] = key[r][c]

    return rotateKey

rotate90(key)
