import math

X,Y,D,T = map(int, input().split())
#1 걸을 때
d1 = (X**2 + Y**2) ** 0.5

#2 점프+걷기
t = max(d1//D,1) #0,0 에 가기 전까지의 최대 점프
d2 = min(t*T + abs(d1-t*D),(t+1)*T + abs((t+1)*D-t)) #0,0에 그전가까이가고 걸어가기, 0,0 그후 까지가고 다시 걸어돌아오기

#3 점프만 (2번 이상 점프)
d3 = max(math.ceil(d1/D),2) * T
print(min(d1,d2,d3))

