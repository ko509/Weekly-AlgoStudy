from itertools import product
def solution(users, emoticons):
    answer = [0,0]
    percent = [40,30,20,10]
        
        
    result = []
    for combination in product(percent, repeat=len(emoticons)): #1차적으로 퍼센트를 2개씩 뽑고
        result.append(list(zip(emoticons,combination))) #2차적으로 같이 엮어준다
    
    
    for p in result:
        money_cnt = 0
        plus_cnt = 0
        for i in users:
            per, money = i[0], i[1]
            total = 0
            for em in p:
                if per <= em[1]: #이상이면 구매
                    total += em[0]/100*(100-em[1])
                    
            
            if total >= money: #이상이면 플러스 구매
                plus_cnt +=1
            else:
                money_cnt+= total
        
        if answer[0] < plus_cnt or (answer[0] == plus_cnt and answer[1] < money_cnt):
            answer = [plus_cnt, money_cnt]

        
    
    return answer
