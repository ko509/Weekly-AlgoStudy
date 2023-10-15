from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

def dfs(n):
    global cnt

    visited[n] = 1
    cycle_list.append(n)

    if visited[choice[n]]:
        if choice[n] in cycle_list:
            cnt -= len(cycle_list[cycle_list.index(choice[n]):])
        return
    else:
        dfs(choice[n])


T = int(input())
for _ in range(T):
    n = int(input())
    choice = [0] + list(map(int, input().split()))

    visited = [0] * (n + 1)
    cnt = n

    for i in range(1, n + 1):
        if not visited[i]:
            cycle_list = []
            dfs(i)

    print(cnt)
