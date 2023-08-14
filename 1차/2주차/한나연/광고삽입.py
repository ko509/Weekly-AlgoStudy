def str2int(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:])
    
    return hour+minute+second

def int2str(time):
    hour = str(time // 3600).zfill(2)
    minute = str(time % 3600 // 60).zfill(2)
    second = str(time % 3600 % 60).zfill(2)
    
    return hour+":"+minute+":"+second

def solution(play_time, adv_time, logs):
    dp = [0] * (str2int(play_time) + 1)
    
    for i in logs:
        temp = i.split('-')
        start = str2int(temp[0])
        end = str2int(temp[1])
        dp[start] += 1
        dp[end] -= 1
        
    for i in range(1, str2int(play_time)):
        dp[i] = dp[i] + dp[i-1]
    for i in range(1, str2int(play_time)):
        dp[i] = dp[i] + dp[i-1]
    
    max_value = -1
    answer = 0
    for i in range(str2int(adv_time)-1, str2int(play_time)):
        temp = dp[i] - dp[i-str2int(adv_time)] 
        if temp > max_value:
            max_value = temp
            answer = i-str2int(adv_time) + 1
            
    return int2str(answer)