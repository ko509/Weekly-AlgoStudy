N = int(input())
data = list(map(int, input().split()))
answer = [0, 0]
data.sort() # 정렬하기
value = int(1e9)*2
left, right = 0, N-1
while left < right:
    temp = data[left] + data[right]
    if abs(value) > abs(temp):
        value = abs(temp)
        answer[0], answer[1] = data[left], data[right]

    if temp < 0:
        left += 1
    else:
        right -= 1


answer.sort() # 오름차순
print(*answer)