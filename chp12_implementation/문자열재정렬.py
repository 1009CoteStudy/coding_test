# 다시 풀어보기 #
data = input()

result = []  # 알파벳 저장
value = 0    # 숫자 저장

## 문자 하나씩 확인
for x in data:
    # 알파벳인 경우 - isalpha()
    if x.isalpha():
        result.append(x)
    # 숫자인 경우
    else:
        value += int(x)

## 알파벳 오름차순 정렬
result.sort()

## 숫자가 존재하면 삽입
if value != 0:
    result.append(str(value))

# 문자열로 변환 후 출력
print(''.join(result))