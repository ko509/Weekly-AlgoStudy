# https://www.acmicpc.net/problem/6051
import sys
import copy
input = sys.stdin.readline

N = int(input())
query = []
log = [[] for _ in range(N+1)]# 모든 기록
stack = [] # 가장 최근에 푼 문제 = 스택 맨 위

for idx in range(N):
    data = list(input().split())
    command = data[0]
    top = 0
    # print(stack)
    if command == 'a': # add
        k = int(data[1])
        stack.append(k)
        log[idx+1].extend(stack)
        top = stack[-1]
    elif command == 's': # delete
        if stack:
            stack.pop()
        if stack:
            log[idx+1].extend(stack)
            top = stack[-1]
        else:
            top = -1

    else: # t
        k = int(data[1])
        stack = copy.deepcopy(log[k-1])
        log[idx+1].extend(stack)
        if stack:
            top = stack[-1]
        else:
            top = -1

    print(top)