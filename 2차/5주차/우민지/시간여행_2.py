import sys
input = sys.stdin.readline

N = int(input())

# query 순서
stack = [[-1, 0]] * (N+1) # value , 바로 앞의 query 번호

j = 0 # 현재 가리키는 stack 부분
for idx in range(1, N+1):
    cmd = list(input().split())

    if cmd[0] == 's': # delete
        stack[idx] = [stack[j][0], j] # 이전 index로 돌아가기
        j = stack[j][1]
    else:
        k = int(cmd[1])
        if cmd[0] == 'a': # add
            stack[idx] = [k, j] #
            j = idx # 현재 가리키는 index
        else: # time warp
            stack[idx] = [stack[j][0], j]
            j = stack[k][1]

    print(stack[j][0]) # value 출력하기
