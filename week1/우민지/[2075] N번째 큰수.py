N = int(input())

array = []
for i in range(N):
    array.extend(list(map(int, input().split())))
array.sort(reverse=True)
print(array[N-1])