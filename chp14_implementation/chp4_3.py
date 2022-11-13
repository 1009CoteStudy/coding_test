# 왕실의 나이트
data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1 # 문자 -> 숫자, ord()

# 8가지 경우 : 방향벡터 사용 #
steps = [(-2,-1),(-2,1),(1,-2),(1,2),(-1,-2),(-1,2),(2,-1),(2,1)]

cnt = 0
for step in steps:
    n_row = row+step[0]
    n_col = col+step[1]

    # 이동이 가능한 경우
    if n_row>=1 and n_row<=8 and n_col>=1 and n_col<=8:
        cnt += 1
print(cnt)