# https://www.acmicpc.net/problem/3020

n, h = map(int, input().split()) # 구간의 개수 h 개
array = []
# n 이 200만개 이므로 O(n) 은 어려움

min_value = n # 장애물 최솟값
count = 0

up = []
down = []

for i in range(n):
    if i % 2 == 1: # down
        down.append(int(input()))
    else: # up
        up.append(int(input()))

# 이분 탐색 이전에 정렬하기 nlog(n)
up.sort() # 1 3 5
down.sort() # 1 3 5

def binary_search(data, height):
    left = 0
    right = len(data) # index
     # height 보다 같거나 작은 중간값을 찾은 후 count 하기
    while left < right:
        mid = (left + right) // 2
        if data[mid] <= height:
            left = mid + 1
        else:
            right = mid -1
    print("data height, right", data, height, right)
    return len(data) - right

for height in range(1, h+1): # 기준점
    up_cnt = binary_search(up, height)
    down_cnt = binary_search(down, h - height)
    temp_cnt = up_cnt + down_cnt
    if temp_cnt < min_value: # 최솟값 갱신
        min_value = temp_cnt
        count = 1
    elif temp_cnt == min_value:
        count += 1
    print("min_value, count",min_value, count)

print(min_value, count)
