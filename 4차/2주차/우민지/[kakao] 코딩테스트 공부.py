# https://school.programmers.co.kr/learn/courses/30/lessons/118668
def solution(alp, cop, problems):
    INF = int(1e9)
    max_alp = 0  # 목표 알고력
    max_cop = 0  # 목표 코딩력
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)  # 최대 필요한 알고력
        max_cop = max(max_cop, cop_req)

    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0  # 초기 알고력, 코딩력

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 알고력 1 높이기, 시간 1 소요
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            # 코딩력 1 높이기, 시간 1 소요
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            # problems list에서 문제 하나 선택하여 알고력 & 코딩력 높이기
            # '최소 소요 시간' 인 경우 고르기

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    if i + alp_rwd <= max_alp and j + cop_rwd <= max_cop:
                        dp[i + alp_rwd][j + cop_rwd] = min(dp[i][j] + cost,
                                                           dp[i + alp_rwd][j + cop_rwd])

    return dp[-1][-1]  # 목표 알고력, 코딩력에 도달하기까지 걸리는 시간