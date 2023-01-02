# 두 배열의 원소 교체

# 아이디어 : 배열 A의 가장 작은 원소와 배열 B의 가장 큰 원소 exchange

# 입력 받기
n, k = map(int,input().split())
# 두 배열은 리스트 형태로 입력 받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 정렬
a.sort()  # 오름차순
b.sort(reverse=True) # 내림차순

# k번 교환
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: break

print(sum(a))