#결국 못풀었습니다ㅠㅠㅠㅠㅠ
#인터넷에 답도 없어서...ㅠㅠㅠ
#우선 완탐으로 풀어서 시간초과나고
#이분탐색같은 경우는 어디서 이분탐색을 써야할지 감이 안오네용... 

N, T = map(int, input().split())
L = list(map(int, input().split()))
#L.sort()
G = []
max_end = 0
for a in L:
    tmp = (a,a+T-1)
    min_tmp = float("inf")
    
    for t in range(T):
        new_start = a-t
        new_end = a+T-1-t
        gap = 0
        for g in G:
            start, end = g
            
            if not (end < new_start or new_end < start): #겹침
                gap += min(end,new_end) - max(start,new_start) + 1
            
        if gap == 0:
            tmp = (new_start,new_end)
            break
        
        if gap < min_tmp :
            min_tmp = gap
            tmp = (new_start,new_end)
            
    G.append(tmp)
    max_end = max(max_end,new_end)
    
max_day = 0
for i in range(1, max_end + 1):
    day = sum(1 for g in G if g[0] <= i <= g[1])
    max_day = max(max_day, day)
            


print(max_day)
    
    
    
            
        
    
                
        