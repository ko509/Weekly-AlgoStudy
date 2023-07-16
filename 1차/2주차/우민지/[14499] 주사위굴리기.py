# https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())
# 지도에 쓰여 있는 수
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
# 명령
command = list(map(int, input().split()))
# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

'''
  2
4 1 3
  5
  6
'''

dice = [0] * 6  # [1,2,3,4,5] (문제에서 전개도 )

def move_dice(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: # 동 [4,2,1,6,5,3]
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: # 서 [3,2,6,1,5,4]
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: # 북 [5, 1, 3, 4, 6, 2]
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: # 남 [2, 6, 3, 4, 1, 5]
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in command:
    nx = x + dx[i-1]
    ny = y + dy[i-1]

    if not (0 <= nx < n and 0 <= ny < m):
        continue
    move_dice(i) # dice 조정하기
    if board[nx][ny] == 0: # dice -> board 숫자 옮기기
        board[nx][ny] = dice[5]
    else: # board -> dice 숫자 옮기기
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny # 갱신
    print(dice[0])

