# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    """
    자연수 n개로 합이 s인 수 만들기
    각 숫자의 크기가 비슷해야 곱이 최대가 됨
    """
    if n > s:
        return [-1]

    n1, n2 = divmod(s, n)
    result = [n1] * n
    for i in range(n2):
        result[i] += 1

    return sorted(result)

if __name__ == "__main__":
    # n = 2
    # s = 9
    n = 2
    s = 8
    result = solution(n, s)
    print(result)