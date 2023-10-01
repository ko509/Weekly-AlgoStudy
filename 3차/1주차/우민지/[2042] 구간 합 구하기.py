# https://www.acmicpc.net/problem/2042
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
data = []
tree = [0] * (N*4)  # data 개수가 N 개 일 때 N 보다 큰 가장 가까운 제곱수 * 2 배

def init_tree(start, end, index):
    if start == end: #leaf node
        tree[index] = data[start-1]
        return tree[index]

    # 재귀적으로 트리를 두 부분으로 나눈 후 그 합을 자기 자신 node 값으로 한다.
    mid = (start+end)//2
    tree[index] = init_tree(start, mid, index*2) + init_tree(mid+1, end, index*2+1)
    return tree[index]

# tree 에서 노드 값 찾기
def find_tree(start, end, index, i, j):
    # i ~ j 범위가 start-end 범위를 초과하는 경우
    if start > j or end < i:
        return 0

    # i ~ j 범위가 start-end 범위 내에 있는 경우
    if i <= start and end <= j:
        return tree[index]

    mid = (start + end)//2
    prefix = find_tree(start, mid, index*2, i, j) + find_tree(mid+1, end, index*2+1, i, j)
    return prefix

# tree 에서 노드 값 업데이트
def update_tree(start, end, index, new_index, new_value):
    if start > new_index or new_index > end:
        return # 트리 범위 초과 시 종료
    tree[index] += new_value

    # leaf node 도달 : 재귀 함수 탈출
    if start == end:
        return
    mid = (start + end) // 2
    update_tree(start, mid, index*2, new_index, new_value)# left
    update_tree(mid+1, end, index*2+1, new_index, new_value)# right


for _ in range(N):
    data.append(int(input()))

init_tree(1, N, 1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        # 원래 있던 노드와의 값 차이만큼만 업데이트 하기
        diff = c - data[b-1]
        data[b-1] = c
        # 구간 합 노드들을 모두 update
        update_tree(1, N, 1, b, diff)

    else: # a == 2 -> 구간 합 구하기
        print(find_tree(1, N, 1, b, c))