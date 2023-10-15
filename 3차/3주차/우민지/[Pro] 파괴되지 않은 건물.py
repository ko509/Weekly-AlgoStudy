# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0

    n = len(board)
    m = len(board[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = (-1) * degree
        dp[r1][c1] += degree
        dp[r2 + 1][c1] -= degree
        dp[r1][c2 + 1] -= degree
        dp[r2 + 1][c2 + 1] += degree
    # 누적합 계산
    for i in range(n):
        for j in range(m):
            dp[i + 1][j] += dp[i][j]

    for i in range(n):
        for j in range(m):
            dp[i][j + 1] += dp[i][j]

    for i in range(n):
        for j in range(m):
            if board[i][j] + dp[i][j] > 0:
                answer += 1
    return answer