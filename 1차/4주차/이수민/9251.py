##LCS알고리즘
##https://chanhuiseok.github.io/posts/algo-34/#%EC%B0%BE%EC%95%84%EB%82%B8-%EA%B7%9C%EC%B9%99
##DP란.....

S1 = input()
S2 = input()
DP = [[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]

M = 0

for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            DP[i+1][j+1] = DP[i][j] + 1
        else :
            DP[i+1][j+1] = max(DP[i+1][j], DP[i][j+1])
    
    M = max(max(DP[i+1]),M)

print(M)
