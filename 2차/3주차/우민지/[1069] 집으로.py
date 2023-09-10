X,Y,D,T = map(int, input().split())
# T초에 D칸 만큼 이동함

answer = int(1e9) # 시간

# 대각선 거리를 구해야 함 !
distance = (X**2 + Y**2) ** 0.5 # 그냥 걷기

if distance >= D: # 1칸씩 이동
    answer = min(distance,
                 T * (distance // D +1),
                 T * (distance //D) + distance % D)
else: # 걷기, 점프한다음에 남은거리 걷기, 점프
    answer = min(distance,
                 T + D-distance ,
                 2*T)
print(answer)