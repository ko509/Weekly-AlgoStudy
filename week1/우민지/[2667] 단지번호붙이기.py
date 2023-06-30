from collections import deque
import heapq

answer = []

n = int(input())
array = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    array.append(list(map(int, input().split())))

