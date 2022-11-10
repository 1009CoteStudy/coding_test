# 내 정답
# 틀렸다고는 하는데 예외를 찾지 못했음
# 백준의 예시는 다 맞음(3190번) 근데 틀리대 ㅠㅠ..
def changeDir(cur, dir): # 방향 전환
    if dir == 'r':
        if cur == 3:
            return 1
        elif cur == 2:
            return 0
        elif cur == 1:
            return 2
        else:
            return 3
    else:
        if cur == 3:
            return 0
        elif cur == 2:
            return 1
        elif cur == 1:
            return 3
        else:
            return 2

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

appleLoc = [] # 사과 좌표

for _ in range(K):
    x, y = map(int, input().split())
    appleLoc.append((x, y))
    
L = int(input()) # 뱀의 방향 변환 횟수

change_dir = [] # 뱀의 방향 변환 저장할 배열

for _ in range(L):
    x, c = input().split()
    change_dir.append((x, c))

sec = 0 # 시간
hx, hy = 1, 1 # 뱀의 머리 위치
tx, ty = 1, 1 # 뱀의 꼬리 위치
cur_h_dir = 3 # 뱀의 머리가 현재 바라보는 방향 # default 오른쪽
cur_t_dir = 3 # 뱀의 꼬리가 현재 바라보는 방향 # default 오른쪽

snake_coord = [(1, 1)] # 뱀이 차지하고 있는 좌표들

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

while True:
    sec += 1 # 1초 증가
    
    # 이동할 내용
    dx = dir[cur_h_dir][0]
    dy = dir[cur_h_dir][1]
    
    # 머리 이동
    hx += dx
    hy += dy
    
    # 벽에 닿았거나 본인의 몸과 부딪히면 종료
    if hx > N or hy > N or hx < 1 or hy < 1 or (hx, hy) in snake_coord:
        break
    
    # 뱀의 경로에 현재 머리 위치 추가
    snake_coord.append((hx, hy))
    
    # 머리가 사과를 안먹었을 경우
    if (hx, hy) not in appleLoc:
        # 꼬리가 있던 위치의 좌표 삭제
        del snake_coord[0]

        dx_t = dir[cur_t_dir][0]
        dy_t = dir[cur_t_dir][1]
        
        tmp_tx = tx + dx_t
        tmp_ty = ty + dy_t
        
        # 방향이 바뀔 경우
        if (tmp_tx, tmp_ty) not in snake_coord:
            # 오른쪽 체크
            check_dir = changeDir(cur_t_dir, 'r')
            
            dx_t = dir[check_dir][0]
            dy_t = dir[check_dir][1]
            
            tmp_tx = tx + dx_t
            tmp_ty = ty + dy_t
            
            # 오른쪽으로 바꿨더니 길이 있을 경우
            if (tmp_tx, tmp_ty) in snake_coord:
                cur_t_dir = check_dir
                tx = tmp_tx
                ty = tmp_ty
            else:
                # 없을 경우왼쪽 체크
                # 여기까지 왔으면 왼쪽으로 이동한건 무조건
                cur_t_dir = changeDir(cur_t_dir, 'r')
            
                dx_t = dir[cur_t_dir][0]
                dy_t = dir[cur_t_dir][1]
                
                tx += dx_t
                ty += dy_t
                
        # 방향이 바뀌지 않았을 경우
        else:
            tx = tmp_tx
            ty = tmp_ty
                
    # 사과를 먹었을 경우엔 꼬리는 움직이지 않는다.
    # 인터넷에 찾아보니 한 번 먹은 사과는 다시 먹을 수 없다고 한다. (슈퍼마리오 생각하면 당연한거 같기도)
    else:
        for apple in appleLoc:
            if apple[0] == hx and apple[1] == hy:
                del apple
                break
        
    
    # 뱀의 이동 경로가 바뀌었을 경우
    # 머리의 방향만 바꿔주고 이동하지는 않는다.
    if len(change_dir) > 0 and sec == int(change_dir[0][0]):
        # 오른쪽으로 90도
        if change_dir[0][1] == 'D':
            cur_h_dir = changeDir(cur_h_dir, 'r')
        else: # 왼쪽으로 90도
            cur_h_dir = changeDir(cur_h_dir, 'l')

        change_dir.pop(0)
                    
print(sec)


# 정답 코드
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
    
# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
        
    return direction
    
def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음은 동쪽 보는 중
    time = 0
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 죽지 않는 경우라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 이동한 곳에 사과가 없다면
            if data[nx][ny] == 0:
                # 이동
                data[nx][ny] = 2
                q.append((nx, ny))
                # 꼬리 제거
                px, py = q.pop()
                data[px][py] = 0
                
            # 사과가 있다면
            if data[nx][ny] == 1:
                # 이동만
                data[nx][ny] = 2
                q.append((nx, ny))
             
        # 벽이나 자신에게 부딪히면   
        else:
            time += 1
            break
        
        x, y = nx, ny # 머리를 실제로 이동
        
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
            
    return time

print(simulate())