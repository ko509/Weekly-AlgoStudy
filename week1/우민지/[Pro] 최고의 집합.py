def solution(n, s):
    answer = []
    if n > s:  # 나눌 수 없는 경우
        return [-1]
    # 원소들 끼리의 차이가 가장 적도록 만들어야 함
    x = s // n
    for i in range(n):
        answer.append(x)
        s -= x
    if s > 0:
        for i in range(n):
            s -= 1
            answer[i] += 1
            if s == 0:
                break

    return sorted(answer)