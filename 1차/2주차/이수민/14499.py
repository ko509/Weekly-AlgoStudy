def move_dice(m,dice):
    a,b,c,d,e,f  = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if m == 1 : #동쪽
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    if m == 2: #서쪽
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    if m == 3 : #북쪽
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e
    if m == 4:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    return dice


N,M,x,y,K = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))

my = list(map(int, input().split()))
dice = [0,0,0,0,0,0] 
move = {1 : (0,1),2:(0,-1),3:(-1,0),4:(1,0)}
for m in my:
    dx, dy = move[m]
    new_x, new_y = x+dx, y+dy
    #지도 바깥으로 이동
    if not (0 <= new_x < N and 0 <= new_y < M):
        continue
    
    dice = move_dice(m,dice)
    if Map[new_x][new_y] == 0 :
        Map[new_x][new_y] = dice[0]
    else :
        dice[0] = Map[new_x][new_y]
    
    print(dice[5])
    x,y = new_x, new_y
    

        