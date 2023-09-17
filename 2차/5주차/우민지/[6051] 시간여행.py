# https://www.acmicpc.net/problem/6051

N = int(input())
query = []
log = [[] for _ in range(N+2)]# 모든 기록
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
        if len(stack) > 1:
            stack.pop()
            log[idx+1].extend(stack)
            top = stack[-1]
        else:
            print(-1)
            continue
    else: # t
        k = int(data[1])
        tmp = log[k-1]
        log[idx+1].extend(tmp)
        stack = tmp
        top = tmp[-1]

    print(top)
