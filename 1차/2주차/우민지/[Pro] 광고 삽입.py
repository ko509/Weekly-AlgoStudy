#https://school.programmers.co.kr/learn/courses/30/lessons/72414

def calc_to_sec(p_time):
    hh, mm, ss = map(int, p_time.split(':'))
    result = hh * 3600 + mm * 60 + ss
    return result


def calc_to_string(p_time):  # p_time 은 seconds
    hh = p_time // 3600
    p_time -= hh * 3600
    mm = p_time // 60
    p_time -= mm * 60
    ss = p_time

    result = ''
    if hh < 10:
        result += '0' + str(hh) + ':'
    else:
        result += str(hh) + ':'

    if mm < 10:
        result += '0' + str(mm) + ':'
    else:
        result += str(hh) + ':'

    if ss < 10:
        result += '0' + str(ss)
    else:
        result += str(ss)

    return result


def solution(play_time, adv_time, logs):
    answer = ''  # min value
    p_time = calc_to_sec(play_time)

    time_bar = [0]
    if play_time == adv_time:
        return '00:00:00'

    start_points = []
    logs.sort()
    for log in logs:
        s, e = log.split("-")

    return answer