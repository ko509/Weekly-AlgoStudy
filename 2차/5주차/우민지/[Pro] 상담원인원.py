# https://school.programmers.co.kr/learn/courses/30/lessons/214288
from heapq import heappush, heappop
from itertools import combinations_with_replacement


def solution(k, n, reqs):
    answer = int(1e9)  # 기다린 시간의 최솟값
    # types = [{i: []} for i in range(1, k+1)] # 유형별로 분류하기
    type_list = [{i: []} for i in range(k)]  # type 별 priority queue

    # 1.  n-k 명 멘토 할당하는 모든 경우의 수 구하기
    comb = combinations_with_replacement([i for i in range(k)], r=n - k)  # nCr
    cases = []
    for com in comb:
        temp = [1 for i in range(k)]  # 각 유형당 1명씩 무조건 배치
        for i in com:
            temp[i] += 1
        cases.append(temp)

    for i in range(len(reqs)):
        start, dur, t = reqs[i]
        type_list[t - 1].append([start, start + dur])

    for case in cases:
        total = 0
        # type 별로 처리하기
        for i in range(k):
            t_list = type_list[i]
            for start, end in t_list:
                if mento <= start:  # mento 가 available 한 경우

                else:  # mento 기다려야 하는 경우
                    total += wait

                    # 최솟값 아닌 경우 pass
            if total > answer:
                break

        answer = min(answer, total)

    return answer