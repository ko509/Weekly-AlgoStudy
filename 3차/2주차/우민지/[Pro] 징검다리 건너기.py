# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    left, right = 0, 200000000
    while left <= right:
        s_list = stones  # copy
        mid = (left + right) // 2
        cnt = 0
        for stone in s_list:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break

        # left , right 조정하기
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left
