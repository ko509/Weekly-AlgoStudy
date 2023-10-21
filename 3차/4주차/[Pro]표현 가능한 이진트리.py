# 포화 이진 트리를 탐색
def check_tree(binary):
    root = len(binary) // 2  # mid
    if root == 0:  # leaf node
        return True
    if binary[root] == '0':
        if '1' not in binary:
            return True
        return False
    return check_tree(binary[:root]) and check_tree(binary[root + 1:])


def make_binary(n):
    reversed_binary = []  # 1. 이진수 저장 빈 문자열
    while n != 1:
        reversed_binary.append(str(n % 2))
        n //= 2
    reversed_binary.append("1")
    binary = "".join(reversed_binary[::-1])  # 나머지를 뒤집어서 이진수 만들기
    # 2. 포화이진트리 만들기 (2**0 + 2**1 + 2**2 + 2**3 ..)
    max_binary_tree = 1
    while max_binary_tree < len(binary):
        max_binary_tree = (max_binary_tree + 1) * 2 - 1
    binary = "0" * (max_binary_tree - len(binary)) + binary  # 부족한만큼 0 추가하기
    return binary


def solution(numbers):
    answer = []  # result

    for n in numbers:
        binary = make_binary(n)
        print(binary)
        if check_tree(binary):  # True
            answer.append(1)
        else:
            answer.append(0)

    return answer

# 올바른 트리의 경우 : 부모 0 - 자식 0 는 가능
# 부모 0 - 자식 1 는 틀림
# 부모 1 - 자식 0 가능
# 부모 1 - 자식 1 가능