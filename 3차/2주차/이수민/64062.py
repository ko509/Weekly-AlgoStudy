def find(stones,k,mid):
    cnt = 0
    global N
    for i in range(len(stones)):
 
        
        if stones[i] - mid <= 0 :
            cnt += 1
        else :
            if cnt >= k :
                return False
            cnt = 0
            
    if cnt >= k :
        return False
            
    return True
        



def solution(stones, k):
    N = max(stones)
    left = 0
    right = N
    
    while left <= right:
        mid = (left+right)//2
        if not find(stones, k, mid):
            right = mid -1
        else :
            left = mid + 1
        
    
    return right+1

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
print(solution([200000000,200000000,200000000,200000000,200000000,200000000],4))
print(solution([7, 2, 8, 7, 2, 5, 9], 3))