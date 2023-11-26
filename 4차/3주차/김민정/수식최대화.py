from itertools import permutations
from collections import deque

def calculate(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    elif op == '*':
        return str(int(num1) * int(num2))

def operation(exp, ops):
    nums = deque()
    tmp_num = ''
    
    for i in exp:
        if i.isdigit():
            tmp_num += i
        else:
            nums.append(tmp_num)
            nums.append(i)
            tmp_num = ''
    
    nums.append(tmp_num)
    
    for op in ops:
        stack = []
        
        while len(nums) != 0:
            tmp = nums.popleft()
            if tmp == op:
                stack.append(calculate(stack.pop(), nums.popleft(), op))
            else:
                stack.append(tmp)
        
        nums = deque(stack)
    
    return abs(int(nums[0]))

def solution(expression):
    res = []
    operator = ["+", "-", "*"]
    
    all_ops = permutations(operator)
    
    for ops in all_ops:
        res.append(operation(expression, ops))

    return max(res)