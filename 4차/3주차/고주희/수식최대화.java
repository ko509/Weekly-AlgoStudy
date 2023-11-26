import java.util.*;

class Solution {
    static long max;
    public long solution(String expression) {
        max = Long.MIN_VALUE;
        perm(expression, 0, new boolean[3], new int[3]);
        return max;
    }
    
    static long cal(String exp, int[] priority, int cnt) {
        if(cnt == 3) {
            return Long.parseLong(exp);
        }
        String pattern = "\\*";
        if(priority[cnt] == -1) {
            pattern = "\\+";
        } else if(priority[cnt] == -2) {
            pattern = "\\-";
        }
        String[] str = exp.split(pattern);
        
        if(priority[cnt] == -1) {
            long number = cal(str[0], priority, cnt+1);
            for(int i = 1; i < str.length; i++) {
                number += cal(str[i], priority, cnt+1);
            }
            return number;
        } else if(priority[cnt] == -2) {
            long number = cal(str[0], priority, cnt+1);
            for(int i = 1; i < str.length; i++) {
                number -= cal(str[i], priority, cnt+1);
            }
            return number;
        } else {
            long number = cal(str[0], priority, cnt+1);
            for(int i = 1; i < str.length; i++) {
                number *= cal(str[i], priority, cnt+1);
            }
            return number;
        }
        
    }
    
    static void perm(String exp, int cnt, boolean[] v, int[] priority) {
        if(cnt==3) {
            long result = cal(exp, priority, 0);
            result = Math.abs(result);
            if(result > max) {
                max = result;
            }
            return;
        }
        for(int i = -3; i <= -1; i++) {
            if(v[i + 3]) continue;
            priority[cnt] = i;
            v[i + 3] = true;
            perm(exp, cnt + 1, v, priority);
            v[i + 3] = false;
        }
    }
    
}
