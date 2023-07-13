#https://school.programmers.co.kr/learn/courses/30/lessons/72414

def calc_to_sec(p_time):
    hh, mm, ss = map(int, p_time.split(':'))
    result = hh * 3600 + mm * 60 + ss
    return result


# zfill -> 0 채워주는 함수
def calc_to_string(p_time):  # p_time 은 seconds
    hh = str(p_time // 3600).zfill(2)
    mm = str(p_time % 3600 // 60).zfill(2)
    ss = str(p_time % 3600 % 60).zfill(2)
    return hh + ":" + mm + ":" + ss


def solution(play_time, adv_time, logs):
    answer = 0  # min value

    p_time = calc_to_sec(play_time)

    time_bar = [0] * (p_time + 1)

    for log in logs:
        s, e = log.split("-")
        s_time = calc_to_sec(s)
        e_time = calc_to_sec(e)
        time_bar[s_time] += 1  # 누적합 계산 위치 찍어두기
        time_bar[e_time] -= 1

        # +1 , -1 처리하기
    for i in range(1, p_time):
        time_bar[i] += time_bar[i - 1]
    # 누적합 구하기
    for i in range(1, p_time):
        time_bar[i] += time_bar[i - 1]

    a_time = calc_to_sec(adv_time)  # 광고 시간
    max_value = 0
    for i in range(a_time - 1, p_time):
        temp = time_bar[i] - time_bar[i - a_time]  # 광고 삽입했을 때 누적합
        if temp > max_value:
            max_value = temp
            answer = i - a_time + 1  # 광고 시작 시간

    return calc_to_string(answer)