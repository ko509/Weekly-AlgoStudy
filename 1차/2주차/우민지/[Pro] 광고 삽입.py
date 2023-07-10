def solution(msg):
    answer = []
    word_dict = {chr(i): (i - 64) for i in range(65, 91)}

    n = len(msg)
    w, c = 0, 0  # 현재 입력, 다음 글자
    while True:
        c += 1  # 다음 입력
        if c == n:  # 마지막 인덱스
            answer.append(word_dict[msg[w:c]])
            break
        if msg[w:c + 1] not in word_dict:  # 없는 경우
            word_dict[msg[w:c + 1]] = len(word_dict) + 1
            answer.append(word_dict[msg[w:c]])
            w = c

    return answer