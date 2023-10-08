import java.util.*;
class Solution {
    public int solution(int[] stones, int k) {
        
        int N = stones.length;
        int min = Integer.MAX_VALUE;
        
        int start = 0;
        int end = 0;
        
        for (int s : stones) {
            end = Math.max(s, end);
        }
        
        while(start <= end) {
            
            int mid = (start + end) / 2;
            
            int cnt = 0;
            int max = 0;
            boolean flag = true;
            for (int i = 0; i < N; i++) {
                if(mid >= stones[i]) {
                    cnt++;
                } else {
                    if(cnt >= k) {
                        min = Math.min(min, mid);
                        flag = false;
                        break;
                    }
                    cnt = 0;
                }
            }
            if(cnt >= k) {
                min = Math.min(min, mid);
                flag = false;
            }
            if(flag) start = mid + 1;
            else end = mid - 1;
        }
        
        if(min == Integer.MAX_VALUE) return 0;
        return min;
    }
}
