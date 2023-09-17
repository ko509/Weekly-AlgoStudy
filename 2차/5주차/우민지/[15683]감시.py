import sys
import copy
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
answer = int(1e9) # 사각지대 최소크기

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

c_type = {1: [[0], [1], [2], [3]],
        2: [[0, 1], [2, 3]], # 상-하, 좌-우
        3: [[0,3], [1,3], [0, 2], [1, 2]],
        4: [[0,1,2], [0,1,3], [0,2,3], [1,2,3]],
        5: [[0,1,2,3]]} # 상하좌우

board = []
cctv = [] # [cctv_type, x, y]
total = 0

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 0:
            total += 1
        if 1 <= data[j] <= 5:
            cctv.append([data[j], i, j])
    board.append(data)

answer = N*M


def cctv_check(dir, x, y, board):
    for i in dir:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7 # 방문 표시

def dfs(index, board):
    global c_type, answer, dx, dy
    if index == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += board[i].count(0) # 사각지대는 아직 0

        answer = min(answer, cnt)
        return

    t, x, y = cctv[index]
    temp_board = copy.deepcopy(board) # 원래 보드 복제
    for dir in c_type[t]:
        cctv_check(dir, x, y, temp_board) # cctv 작동
        dfs(index+1, temp_board)
        temp_board = copy.deepcopy(board) # 백트래킹


dfs(0, board)
print(answer)