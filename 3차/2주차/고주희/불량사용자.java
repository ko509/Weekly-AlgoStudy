import java.util.*;

class Solution {
    static int count = 0;
    static boolean[] bit = new boolean[256];
    public int solution(String[] user_id, String[] banned_id) {

        perm(0, new int[banned_id.length], new boolean[user_id.length], user_id, banned_id);
        return count;
    }
    
    static void perm(int cnt, int[] num, boolean[] v, String[] user, String[] ban) {
        
        int N = user.length;
        if(cnt == ban.length) {
            int size = ban.length;
            boolean flag = true;
            for(int i = 0; i < size; i++) {
                if(user[num[i]].length() != ban[i].length()) {
                    flag = false; 
                    continue;
                }
                for(int j = 0; j < ban[i].length(); j++) {
                    if(ban[i].charAt(j) == '*') continue;
                    if(user[num[i]].charAt(j) != ban[i].charAt(j)) flag = false;
                }
            }
            if(flag) {
                int b = 0;
                for(int i = 0; i < size; i++) {
                    b |= (1 << num[i]);
                }
                if(bit[b]) return;
                bit[b] = true;
                count++;
            } 
            
            return;
        }
        
        for(int i = 0; i < N; i++) {
            if(v[i]) continue;
            v[i] = true;
            num[cnt] = i;
            perm(cnt + 1, num, v, user, ban);
            v[i] = false;
        }
    }
}
