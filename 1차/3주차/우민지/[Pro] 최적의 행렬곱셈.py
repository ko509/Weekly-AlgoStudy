def solution(matrix_sizes):
    n = len(matrix_sizes)
    INF = int(1e9)
    dp = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0

    for step in range(1, n):
        for start in range(n):
            end = start + step
            if end >= n:
                break
            for sep in range(start, end):
                dp[start][end] = min(dp[start][end],
                                     dp[start][sep] + dp[sep + 1][end]
                                     + matrix_sizes[start][0] * matrix_sizes[sep][1] * matrix_sizes[end][1])

    return dp[0][n-1]