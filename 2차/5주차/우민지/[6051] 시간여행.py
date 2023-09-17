# https://www.acmicpc.net/problem/6051
import sys
input = sys.stdin.readline

N = int(input())
query = []
log = [[]] # 모든 기록
stack = [] # 가장 최근에 푼 문제 = 스택 맨 위

for idx in range(N):
    data = list(input().split())
    command = data[0]
    top = 0
    # print(stack)
    if command == 'a': # add
        k = int(data[1])
        stack.append(k)
        log.append(stack[:])
        top = stack[-1]
    elif command == 's': # delete
        if stack:
            stack.pop()
        if stack:
            log.append(stack[:])
            top = stack[-1]
        else:
            top = -1
            log.append(stack[:])

    else: # t
        k = int(data[1])
        stack = log[k-1][:]
        log.append(stack[:])
        if stack:
            top = stack[-1]
        else:
            top = -1
    # print(log)
    print(top)