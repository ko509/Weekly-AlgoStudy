# https://school.programmers.co.kr/learn/courses/30/lessons/214288

def solution(k, n, reqs):
    answer = 0  # 기다린 시간의 최솟값
    types = [{i: []} for i in range(1, k + 1)]  # 유형별로 분류하기

    for i in range(len(reqs)):
        start, dur, t = reqs[i]
        types[t - 1].append([start, dur])

    return answer