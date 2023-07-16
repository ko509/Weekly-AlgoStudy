import java.util.*;
/*
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
*/
class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        
        int p_time = get_time(play_time);
        int a_time = get_time(adv_time);
        // System.out.println(p_time + " " + a_time);
        
        long[] watcher = new long[p_time + 1];
        
        // 시청 시간 누적합
        for(String log : logs) {
            String[] watch = log.split("-");
            int start = get_time(watch[0]);
            int end = get_time(watch[1]);
            watcher[start]++;
            if(end <= p_time) watcher[end]--;
        }
        
        for(int i = 1; i <= p_time; i++) {
            watcher[i] += watcher[i-1];
        }
        
        long count = 0l;
        
        for(int i = 0; i < a_time; i++) {
            count += watcher[i];
        }
        
        long max = count;
        int time = 0;

        // 구간 당 보는 사람들
        for(int i = 1; i <= p_time - a_time; i++) {
            count -= watcher[i-1];
            count += watcher[i + a_time - 1];
            if(count > max) {
                time = i;
                max = count;
            }
        }
        String answer = get_string(time);
        return answer;
    }
    
    String get_string(int time) {
        int hour = time/3600;
        time %= 3600;
        int min = time/60;
        time %= 60;
        int sec = time;
        
        StringBuilder sb = new StringBuilder();
        if(hour < 10) sb.append(0);
        sb.append(hour).append(":");
        if(min < 10) sb.append(0);
        sb.append(min).append(":");
        if(sec < 10) sb.append(0);
        sb.append(sec);
        
        return sb.toString();
    }
    
    int get_time(String time) {
        String[] tmp = time.split(":");
        int hour = Integer.parseInt(tmp[0]);
        int min = Integer.parseInt(tmp[1]);
        int sec = Integer.parseInt(tmp[2]);
        
        return hour * 3600 + min * 60 + sec;
    }
}
