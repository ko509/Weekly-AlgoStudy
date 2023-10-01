import sys

input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
answer = 0
dp = [0] * M # 나머지를 저장하는 배열 , size가 M 이 된다.
prefix_sum = 0
for i in range(N):
    prefix_sum += data[i]
    dp[prefix_sum%M] += 1 # 나머지가 몇개인지 저장하기

# 누적합을 M 으로 나누기,
answer = dp[0] # 나머지가 0 인 경우는 무조건 포함시키기

# iC2 조합으로 구하기 , 나머지가 같은 구간 2개를 뽑는 모든 경우의 수
for i in dp:
    answer += i*(i-1)//2
print(answer)