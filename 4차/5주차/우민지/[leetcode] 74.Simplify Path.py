# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150
def simplifyPath(path: str) -> str:
    stack = []
    tokens = path.split("/")
    print(tokens)
    for token in tokens:
        if token == ".." and stack: # 상위 경로로 이동 -> 경로 삭제 !
            stack.pop()
        elif token != ".." and token != "." and token: # ex. home, foo ..
            stack.append(token)

    return "/" + "/".join(stack)
