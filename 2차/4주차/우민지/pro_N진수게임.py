def change_num(x, base): # 숫자, base 진수
    num_str = '0123456789ABCDEF' # 2 ~ 16 진수
    a, b = divmod(x, base) # 몫, 나머지
    if a == 0:
        return num_str[b]
    else:
        return change_num(a, base) + num_str[b]

def solution(n, t, m, p):
    answer = ''
    changed = ''
    # n 진수로 변환하기
    max_value = m * t # 최대 길이
    for i in range(max_value):
        changed += change_num(i, n) # n 진수
    while len(answer) < t: # t 번 반복 (구할 숫자 길이)
        answer += changed[p-1]
        p += m # 참여 인원
    return answer