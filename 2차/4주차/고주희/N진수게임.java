import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        int tmp = 0;
        List<Integer> list = new ArrayList<>();
        list.add(0);
        list.add(0);
        while(tmp < t * m) {
            int a = tmp;
            Stack<Integer> stack = new Stack<>();
            while(a > 0) {
                stack.add(a % n);
                a /= n;
            }
            while(!stack.isEmpty()) {
                list.add(stack.pop());
            }
            tmp++;
        }
        
        // System.out.println(Arrays.toString(list.toArray()));
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < t; i++) {
            int a = list.get(i * m + p);
            // System.out.println(a);
            if(a >= 10) {
                sb.append((char)('A' + (a - 10)));
            }
            else sb.append(a);
        }

        return sb.toString();
    }
}
