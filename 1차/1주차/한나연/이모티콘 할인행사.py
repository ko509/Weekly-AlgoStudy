# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):
    combis = list(product([10,20,30,40], repeat=len(emoticons)))

    answer = [0,0]
    for combi in combis:
        sign_up = 0
        amount = 0
        for rate, limit in users:
            price = 0
            for i, emoticon in enumerate(emoticons):
                if rate <= combi[i]:
                    price += emoticon * (100 - combi[i]) // 100

            if limit <= price:
                sign_up += 1
            else:
                amount += price
        
            answer = max(answer, [sign_up, amount])    
            
    return answer