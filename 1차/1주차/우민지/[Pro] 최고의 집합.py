def solution(n, s):
    answer = []

    if n > s:
        return [-1]
    x = s // n  # 가장 큰 곱을 위한 element

    left = s - x * n
    for i in range(n):
        answer.append(x)
    if left == 0:
        return answer
    else:
        idx = 0
        while left:
            answer[idx] += 1
            left -= 1
            idx += 1

    return sorted(answer)  # 정렬