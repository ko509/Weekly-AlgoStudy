N = int(input())
check = [True] * (N+1) # 1 ~ N
sosu = [] # 소수 list

answer = 0
# 1. 소수 구하기
for i in range(2, N+1):
    if check[i]:
        sosu.append(i)
        for j in range(2*i, N+1, i): # i 의 배수 제거하기
            check[j] = False

print(sosu)

# 2. 경우의 수 구하기 - two pointer
start = 0
end = 0
while end <= len(sosu):
    total = sum(sosu[start:end])
    if total == N:
        answer += 1
        end += 1
    elif total < N:
        end += 1
    else:
        start += 1 # 값이 큰 경우 start pointer 를 옮겨서 값을 줄인다

print(answer)