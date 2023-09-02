from math import sqrt
x, y, d, t = map(int, input().split())
dist = sqrt(x**2 + y**2)
nj = dist//d
rdist = dist - nj*d
####### walk or jump and walk #######
time = min(nj*t + rdist, dist, (nj+1)*t + d - rdist)

#### in triangle inequality, we can go to the goal with n+1 ####
if nj > 0:
    time = min(time, (nj+1)*t)
elif dist < d:
    time = min(time, 2*t)
print(time)