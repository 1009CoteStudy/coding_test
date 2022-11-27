# 회의실 배정
n = int(input())
time = []
for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])




print(time)


# 제혁님 코드
#info = sorted(info, key=lambda x: (x[1], x[0])) : x[1]으로 먼저 오름차순 -> x[0]으로
