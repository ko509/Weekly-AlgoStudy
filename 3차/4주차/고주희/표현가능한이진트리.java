class Solution {
    public int[] solution(long[] numbers) {
        int N = numbers.length;
        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(Long.toBinaryString(numbers[i]));
            int size = sb.length();
            if(size == 1) {}
            else if(size <= 3) {
                while(size < 3) {
                    sb.insert(0, "0");
                    size++;
                }
                size = 3;
            } else if(size <= 7) {
                while(size < 7) {
                    sb.insert(0, "0");
                    size++;
                }
                size = 7;
            } else if(size <= 15) {
                while(size < 15) {
                    sb.insert(0, "0");
                    size++;
                }
                size = 15;
            } else if(size <= 31) {
                while(size < 31) {
                    sb.insert(0, "0");
                    size++;
                }
                size = 31;
            } else if(size <= 63) {
                while(size < 63) {
                    sb.insert(0,  "0");
                    size++;
                }
                size = 63;
            }
            String str = sb.toString();
            if(is_long(str.toCharArray(), 0, size - 1)) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        return answer;
    }
    
    static boolean is_long(char[] c, int start, int end) {
        if(start == end) {
            return true;
        }
        int mid = (start + end) / 2;
        if(c[mid] == '0') {
            for (int i = start; i <= end; i++) {
                if(c[i] == '1') return false;
            }
            return true;
        } else {
            return is_long(c, start, mid - 1) && is_long(c, mid + 1, end);
        }
        
    }
}
