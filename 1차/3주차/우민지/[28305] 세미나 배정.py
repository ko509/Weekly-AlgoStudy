# https://www.acmicpc.net/problem/28305

n, t = map(int, input().split())
array = list(map(int, input().split())) # 반드시 세미나 하는 날 (외부 세미나)
array.sort()  # 3 4 5 6 7
dp = [0] * 200001

def calc(num):
    for i in range(n):
        dp[i] = array[i]

    if num == 0:
        return False
    for i in range(n):
        if i < num:
            if dp[i] >= t: # 연속
                dp[i] = array[i] + 1
            else:
                dp[i] = t + 1
        else:
            if dp[i-num] > array[i]:
                return False
            if dp[i-num] + t <= array[i] + 1:
                dp[i] = array[i] + 1
            else:
                dp[i] = dp[i - num] + t

    return True

def binary_search():
    left = 1
    right = 200000
    mid = (left+right) // 2
    while left < right:
        if calc(mid):
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    if not calc(mid):
        mid += 1
    return mid


print(binary_search())