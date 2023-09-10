# https://www.acmicpc.net/problem/2281
import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
names = [] # 7, 4, 2, 3, 2, 5, 1, 12, 7, 5, 6
# 공간을 넉넉하게
deathnote = [[-1] * m for _ in range(n)] # 최대 n 개 줄 가능, 길이는 m 만큼

for _ in range(n):
    names.append(int(input()))

# 마지막 줄은 공백 무시하기
'''
dp[9] 
1. 5를 쓰고 다음줄에 6쓰기 
2. 5와 6을 같은 줄에 쓰기 

dp[8] 
1. 7을 먼저 쓰고 다음줄에 5,6 쓰기 
2. 7, 5 를 먼저 쓰고 다음 줄에 6 쓰기 
3. 7, 5, 6 을 한 줄에 쓰기 
'''

def dfs(idx, name):
    global deathnote
    if deathnote[idx][name] != -1 :
        return
    if idx == n-1: # 마지막 줄은 제곱 계산 안함
        deathnote[idx][name] = 0
    else:
        # 같은 줄에 쓸 수 있는지 확인하기
        if name + 1 + names[idx+1] < m:
            deathnote[idx][name] = min(
                dfs(idx+1, name+1+names[idx+1]),
                dfs(idx+1, names[idx+1] + (m - name -1) ** 2))
        else: #  줄 바꾸기
            deathnote[idx][name] = dfs(idx+1, names[idx+1] + (m - name -1) ** 2)
    return deathnote[idx][name]

print(dfs(0, names[0]))