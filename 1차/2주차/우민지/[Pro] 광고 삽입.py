#https://school.programmers.co.kr/learn/courses/30/lessons/72414

def get_time(time):
    h, m, s = time.split(':')
    total = int(h) * 3600 + int(m) * 60 + int(s)
    return total


def solution(play_time, adv_time, logs):
    answer = ''  # min value

    if play_time == adv_time:
        return '00:00:00'

    start_points = []
    logs.sort()
    for log in logs:
        s, e = log.split("-")
        start_points.append(s)
    print(start_points)

    return answer