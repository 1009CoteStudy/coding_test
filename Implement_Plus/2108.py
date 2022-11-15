# 실버 3
N = int(input())
datas = []

for i in range(N):
    data = int(input())
    datas.append(data)

# 산술 평균
print(round(sum(datas) / N))

# 중앙값
datas.sort()
print(datas[N // 2])

# 범위
ran = max(datas) - min(datas)

# 최빈값
def printFunc(data):
    print(data - 4000)

# 입력되는 정수의 최댓값은 4000 밑이므로 -4000~4000 데이터를 + 4000 한 인덱스에 카운트를 해주려 한다.
# ... 8000개 두면 O(N^2) 하면 6400만 이라 2초가 넘어가네.. 1초당 2000만이라 치니까 O(NlogN) 안에 풀어야 됨
tmp = [0] * 8002

for data in datas:
    # + 4000 한 인덱스에 카운트
    tmp[data + 4000] += 1

# 최대값이 여러개면
if tmp.count(max(tmp)) > 1:
    # 첫 번째 최대값 삭제
    tmp.remove(max(tmp))
    # 인덱스가 -1씩 됐지만 입력되는 정수가 인덱스로 들어간 것이기 때문에 다시 + 1
    # 처음에 더한 4000만큼 빼서 출력
    print(tmp.index(max(tmp)) + 1 - 4000)
else:
    print(tmp.index(max(tmp)) - 4000)

# 범위 출력
print(ran)