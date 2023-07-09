#Note : 아무리봐도 완탐은 아닌 것 같아서 규칙으로 찾음. 
def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    else:
        i = s//n
        answer = [i for _ in range(n)]
        total = sum(answer)
        index = 0
        while total < s:
            answer[index] += 1
            total+=1
            index+=1
            if index == n:
                index = 0
    answer.sort()
    return answer

print(solution(3,8))