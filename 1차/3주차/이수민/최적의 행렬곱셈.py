##DP...........GG
##답을 봐도 이해못하겠음.............
##포기포기포기!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##아래는 GPT가 해줬습니다....

def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0] * n for _ in range(n)]

    # 행렬 곱셈 크기에 대한 초기화
    for i in range(1, n):
        dp[i - 1][i] = matrix_sizes[i - 1][0] * matrix_sizes[i - 1][1] * matrix_sizes[i][1]

    # 행렬 곱셈 크기를 3개 이상일 때 계산
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])

    return dp[0][n - 1]