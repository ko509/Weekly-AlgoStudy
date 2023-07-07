# https://school.programmers.co.kr/learn/courses/30/lessons/150368

total_member = 0
total_profit = 0
rates = [10, 20, 30, 40]


def calc(rate_list, users, emoticons):
    temp_member = 0
    temp_profit = 0
    for user in users:
        rate, money = user
        user_profit = 0

        for i in range(len(emoticons)):
            if rate_list[i] >= rate:
                user_profit += emoticons[i] * (1 - (rate_list[i] * 0.01))
        if user_profit >= money:
            temp_member += 1
        else:
            temp_profit += user_profit
    return temp_member, temp_profit


def dfs(count, rate_list, users, emoticons):
    global total_member, total_profit, rates

    if count == len(emoticons):
        temp_member, temp_profit = calc(rate_list, users, emoticons)
        if total_member < temp_member:
            total_member = temp_member
            total_profit = temp_profit
        elif total_member == temp_member:
            total_profit = max(temp_profit, total_profit)
        return  # dfs 종료

    for i in range(4):
        dfs(count + 1, rate_list + [rates[i]], users, emoticons)


def solution(users, emoticons):
    global total_member, total_profit
    dfs(0, [], users, emoticons)
    answer = [total_member, total_profit]
    return answer