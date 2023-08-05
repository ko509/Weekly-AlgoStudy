N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
# j 만큼의 cost 를 사용해서 얻는 최대 메모리값 구하기 !
# 앱을 종료하거나 종료하지 않았을 때 경우
dp = [[0] * (sum(cost)+1) for _ in range(N+1)]

answer = int(1e9) # 최소 비용

for i in range(1, N+1):
    for j in range(sum(cost)+1): # 가능한 모든 cost 의 범위 확인 !
        temp_memory = memory[i]
        temp_cost = cost[i]
        if j < cost[i]: # 현재 확인중인 앱의 cost 보다 j 값이 작은 경우 : dp 갱신을 못함
            dp[i][j] = dp[i-1][j]
        else:
            # 비용 j 만큼에서 얻을 수 있는 최대 메모리 값 갱신해주기
            dp[i][j] = max(dp[i-1][j-temp_cost] + temp_memory, dp[i-1][j])

        # cost 갱신하기
        if dp[i][j] >= M:
            answer = min(answer, j)


print(answer)