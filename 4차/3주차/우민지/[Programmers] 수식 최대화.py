from itertools import permutations


def calc(x, y, op):
    if op == '+':
        return str(int(x) + int(y))
    if op == '-':
        return str(int(x) - int(y))
    if op == '*':
        return str(int(x) * int(y))


def check_case(case, expression):
    exp = []  # 문자열을 계산할 수 있도록 전처리
    num = ''
    for i in expression:
        if i.isdigit():
            num += i
        else:  # 연산지인 경우
            exp.append(num)
            num = ''  # 초기화
            exp.append(i)
    exp.append(num)

    # ex. case = ['*', '+', '-']
    # case 순서대로  연산 처리하기 - (인덱스 작을 수록 우선 순위 높음)
    for op in case:
        stack = []
        while exp:
            now = exp.pop(0)
            if now == op:  # 이번 우선순위에서 확인하는 연산자이면
                x = stack.pop()  # 스택 맨 위에 쌓여있는 숫자 꺼내기
                y = exp.pop(0)  # 숫자하나 더 꺼내기
                stack.append(calc(x, y, op))
            else:  # 숫자 or 우선순위에 밀리는 연산자의 경우
                stack.append(now)
        exp = stack  # 중위 표현식 갱신하기

    return abs(int(exp[0]))


def solution(expression):
    answer = 0  # 절댓값
    ops = ['+', '-', '*']

    ops_arr = list(permutations(ops, 3))

    for case in ops_arr:
        result = check_case(case, expression)
        answer = max(answer, result)

    return answer