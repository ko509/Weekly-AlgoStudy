#처음높이에서 가장 큰 높이가 오기 전까지는 같거나 올라가기만해야함. 그 이후에는 같거나 내려오기만 해야하며 마지막 높이보다 작게 내려갈 수 없다.

N = int(input())
S = []
max_h = 0
for _ in range(N):
    w,h = map(int, input().split())
    max_h = max(max_h,h)
    S.append([w,h])

S.sort(key=lambda x:x[0])
s = 0
cur_h = S[0][1]
cnt = S[0][0]
total = 0

for i in S:
    w,h = i[0],i[1]
    
    
    if h <= max_h: #가장 큰 높이 전
        if cur_h < h : #현재 높이보다 클 때->즉, 높이가 높게 바뀌어 그전것들을 계산할 때
            total += (w-cnt) * cur_h
            cur_h = h
            cnt = w
    
    if h == max_h :
        s = w#가장 높은 것을 만났을 때의 x좌표 저장
        break
    
    
#올라가는건 쉽게 구현하겠는데, 내려가는 부분은 바로 안나와서 그냥 뒤집어서 다시 해버렸다.
cur_h = S[-1][1]
cnt = S[-1][0]
n = 0
for i in S[::-1]:
    w,h = i[0],i[1]
    
    
    if h <= max_h: 
        if cur_h < h : 
            total += (cnt - w) * cur_h
            cur_h = h
            cnt = w
    
    if h == max_h :
        n = w#가장 높은 것을 만났을 때의 x좌표 저장
        break
    
total += (n-s+1)*max_h #가장 높은 길이 개수 * 높은 길이
print(total)            
            
        
