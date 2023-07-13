# https://school.programmers.co.kr/learn/courses/30/lessons/17684

"""
알파벳 중 가장 긴 알파벳부터 사용해 압축해야 하기 때문에
msg 전부 → msg 뒤쪽을 줄여가면서 사전에 존재하는지 확인한다.
    사전 안에 알파벳이 존재하면 answer에 인덱스를 추가하고,
    없으면 바로 직전 문자열을 사전에 추가한다.
"""
def solution(msg):
    # {알파벳:인덱스} 정보가 들어있는 사전 초기화        
    dic = {}
    for i in range(26):
        dic[chr(i+65)] = i+1

    answer = []
    index = 27  # 다음 인덱스
    while(msg):
        char_len = 0
        curr_msg, prev_msg = msg, msg  # 현재 탐색할 문자열, 사전에 추가할 문자열

        while(curr_msg):
            # 현재 문자열이 사전에 존재하면 정답 리스트에 인덱스 append
            if curr_msg in dic:
                answer.append(dic[curr_msg])
                dic[prev_msg] = index  # 바로 직전 문자열 사전에 추가
                index += 1
                char_len = len(curr_msg)
                break
            # 현재 문자열이 사전에 존재하지 않으면 문자열 한 글자 줄이기
            else:
                prev_msg = curr_msg
                curr_msg = curr_msg[:-1]
        
        # 이미 정답 리스트에 추가한 알파벳 삭제
        msg = msg[char_len:]

    return answer