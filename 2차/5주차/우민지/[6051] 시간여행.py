# https://www.acmicpc.net/problem/6051

N = int(input())
query = []
log_stack = [[-1]] # 모든 기록
stack = [] # 가장 최근에 푼 문제 = 스택 맨 위
for idx in range(N):
    data = list(input().split())
    if len(data) == 1:  # s 연산
        if len(stack) > 0:
            top = stack[-1]
            stack.pop()
        else:
            print(-1)
            continue # 다음 query 로 넘기기
    else:  # a, t 연산
        command, k = data[0], int(data[1])
        if command == 'a':
            stack.append(k)
            top = stack[-1]
        else: # command == 't'
            stack = log_stack[k-1]
            top = stack[-1]
        print(top)
    log_stack.append(stack)




