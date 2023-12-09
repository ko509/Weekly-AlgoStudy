# https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        N = len(board[0])
        M = len(board)

        island = set()  # O 를 섬으로 취급

        # 내부에 있는 O 확인하기
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    island.add((i, j))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # BFS

        def bfs(x, y):
            queue = deque([])
            queue.append((x, y))
            visited[x][y] = True
            while queue:
                x, y = queue.popleft()
                island.discard((x, y))  # 가장자리는 X 처리에서 제외 필요함
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == "O" and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

        visited = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if (i == M - 1 or i == 0 or j == N - 1 or j == 0):
                    if not visited[i][j] and board[i][j] == "O":
                        print(i, j)
                        bfs(i, j)

        # O -> X flip
        for x, y in island:
            board[x][y] = "X"