n, m = map(int, input().split())
S = [0]
for _ in range(n):
    S.append(int(input()))
    
DP = [0 for _ in range(n+2)]

for i in range(n-1,0,-1): #뒤에서 부터 시작
    a = (m-S[i])**2 + DP[i+1]#얘만 새로운 줄에 
    DP[i] = a
    tmp = m - S[i]
    
    for j in range(i+1,n+1): # 그 다음 것까지 같은줄에 넣을 수 있는지, 같은 줄에 넣을 수 있을 때까지 계산
        tmp -= S[j]
        tmp -= 1
        if tmp >= 0 : #넣을 수 있다면
            if j == n : #마지막줄이 되면 무조건 0
                DP[i] = 0
                break
            
            DP[i] = min(DP[i],tmp**2 + DP[j+1]) # 그전 것과 이번꺼 비교해서 작은것
        else :#못넣는다면 그 뒤도 못넣으니까 나오기
            break
        
    
print(DP[1]) #첫번째 줄은 무조건 새로운줄에서 시작하므로, 첫번째줄에서의 최소값을 구하면 됨.
    