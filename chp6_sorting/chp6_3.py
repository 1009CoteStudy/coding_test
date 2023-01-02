# 성적이 낮은 순서로 학생 출력하기
n = int(input())

# 한 쌍의 데이터 입력 받기
array = []
for i in range(n):
    student = input().split()
    # 두 원소를 리스트로 묶어야함, 정수형은 변환 후 저장
    array.append( (student[0], int(student[1])) )

# key를 기준으로 오름차순으로 정렬
result = sorted(array, key = lambda x : x[1])

# 출력
## result 내부 : [('나', 2), ('너', 4)]
for x in result:  # result 내부의 리스트 한 쌍이 x
    print(x[0], end=' ')