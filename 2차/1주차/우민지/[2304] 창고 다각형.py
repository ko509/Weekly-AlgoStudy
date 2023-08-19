
n = int(input())
array = []

maxHeight = 1
maxLength = 0

for i in range(n):
    x, y = map(int, input().split())
    array.append([x ,y])
    if maxLength < x:
        maxLength = x
    if maxHeight < y:
        maxHeight = y
        maxIndex = x

total = 0
temp = 0

result_array = [0] * (maxLengt h +1)
for l, h in array:
    result_array[l] = h # 딕셔너리 형태로 저장한다

for i in range(maxIndex + 1):
    if result_array[i] > temp:
        temp = result_array[i]
    total += temp

temp = 0

for i in range(maxLength, maxIndex, -1):
    if result_array[i] > temp:
        temp = result_array[i]
    total += temp
print(total)