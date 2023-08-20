n = int(input())

data = list(map(int, input()))
result = list(map(int, input()))

# deep copy
temp1 = data[:]
temp2 = data[:]
count = 0

# index 0 부터 시작
def from_zero(temp):
    count = 1
    temp[0] = int(not temp[0])
    temp[1] = int(not temp[1])
    for i in range(1, n):
        # 비교해서 바꿔주어야 하면 클릭하기
        if result[i-1] != temp[i-1]:
            count += 1
            temp[i-1] = int(not temp[i-1])
            temp[i] = int(not temp[i])
            if i != n-1:
                temp[i+1] = int(not temp[i+1])
    if temp == result:
        return count
    return -1
# index 1부터 시작
def from_one(temp):
    count = 0
    for i in range(1, n):
        # 비교해서 바꿔주어야 하면 클릭하기
        if result[i-1] != temp[i-1]:
            count += 1
            temp[i-1] = int(not temp[i-1])
            temp[i] = int(not temp[i])
            if i != n-1: # 인덱스 초과 예외처리
                temp[i+1] = int(not temp[i+1])
    if temp == result:
        return count
    return -1

a = from_zero(temp1)
b = from_one(temp2)
if a == -1 and b != -1:
    print(b)
elif a != -1 and b == -1:
    print(a)
else:
    print(min(a, b))