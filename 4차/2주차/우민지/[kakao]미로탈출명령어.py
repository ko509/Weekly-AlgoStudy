from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    board = [['.'] * m for _ in range(n)]
    x, y, r, c = x - 1, y - 1, r - 1, c - 1

    def get_distance(a, b):
        return abs(a - r) + abs(b - c)

    board[x][y], board[r][c] = 'S', 'E'
    # 주의) 탐색 방향을 사전순으로 해야 한다 d, l, r, u
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    literal = ['d', 'l', 'r', 'u']
    # 최단거리가 k 보다 작거나 ( 최단거리 - k )가 홀수 인 경우
    if get_distance(x, y) > k or (get_distance(x, y) - k) % 2 == 1:
        return "impossible"

    queue = deque([])
    queue.append([x, y, '', 0])
    while queue:
        x, y, route, step = queue.popleft()
        if board[x][y] == 'E' and (k - step) % 2 == 1:  # 남은 거리가 홀수이면 되돌아 오지 못하므로 탈출 불가능
            return "impossible"
        elif board[x][y] == 'E' and step == k:
            return route

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if get_distance(nx, ny) + step + 1 > k:
                    continue
                queue.append([nx, ny, route + literal[i], step + 1])
                break  # 이미 사전순으로 정렬했으므로 여기서 break 걸어주어야 시간 초과를 방지할 수 있다!
    return answer