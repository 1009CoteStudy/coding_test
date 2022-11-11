# 내 코드
def solution(n, weak, dist):
    answer = 0
    weak_dist = [] # 각 취약점 사이 거리
    
    for i in range(len(weak) - 1):
        weak_dist.append(weak[i + 1] - weak[i])
    
    # 맨 마지막 취약점과 맨 처음 취약점 사이 거리
    weak_dist.append((12 - weak[-1]) + weak[0])
    
    weak_dist.sort()
    
    i = 1
    while True:
        wd_len = len(weak_dist)
        
        if wd_len <= 0:
            answer = -1
            break
        
        weak_dist.pop()
        
		# 취약점 거리의 합 <= dist 뒤에서부터 i번째 사람의 값의 합이면 뭔가 될 것 같았음
        # 그럴리가 없지
        if sum(weak_dist) <= sum(dist[len(dist) - i:]):
            answer = i
            break
        else:
            i += 1
    
    return answer

# 정답 코드
from itertools import permutations # 순열

def solution(n, weak, dist):
    # 길이를 2배로 늘려 원형을 일자 형태로 변경
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최소값을 찾아야 하므로 나올 수 없는 값으로 초기화
    
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대해 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구 수
            position = weak[start] + friends[count - 1] # 해당 친구가 점검할 수 있는 마지막 위치
            
            for index in range(start, start + length): # 시작점부터 모든 취약 지점 확인
                if position < weak[index]: # 점검할 수 있는 위치를 벗어나는 경우
                    count += 1 # 새 친구 투입
                    if count > len(dist): # 더 투입 불가능하면 종료
                        break
                    
                    position = weak[index] + friends[count - 1]
                    
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
        
    return answer