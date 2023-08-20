n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

n = len(nums)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

# 학생수 - 가장 긴 증가하는 부분 수열의 길이
print(n - max(dp))
    

#결국 코드는 아니지만 로직은 본...
#난 멍청해서..학생수 - 가장 긴 증가하는 부분 수열의 길이 와 같은거 생각못하는데...