N = int(input())
check = [True] * (N+1) # 1 ~ N
sosu = [] # 소수 list

# 1. 소수 구하기
for i in range(2, N+1):
    if check[i]:
        sosu.append(i)
        for j in range(i, N+1, i): # i 의 배수 제거하기
            if check[j]:
                check[j] = False

