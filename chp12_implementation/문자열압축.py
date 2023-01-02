# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    res = []

    # block(단위)만큼 늘려가며 확인
    for block in range(1, len(s) // 2 + 1):
        prev = s[0:block]
        compressed = ''
        cnt = 1
        # block(단위)만큼 증가시키며 비교
        for j in range(block, len(s), block):
            # 이전 상태와 동일할 경우
            if prev == s[j:j + block]:
                cnt += 1
            # 다른 문자열이 나올 경우
            else:
                if cnt > 1:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[j:j + block]  ## prev 초기화
                cnt = 1  ## cnt 초기화
        # 마지막 문자열 처리
        if cnt > 1:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        res.append(len(compressed)) # 바로 문자열 길이로 입력

    # 테스트케이스가 1일 때
    if not res: return 1
    else: return min(res)

## 문자열이 값인 리스트의 min을 하면 문자열 비교가 됨
## 문제는 길이 비교
