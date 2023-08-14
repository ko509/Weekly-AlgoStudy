import java.util.*;

/*
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
*/
class Solution {
    public int[] solution(String msg) {
        
        Map<String, Integer> map = new HashMap<>();
        int alpha = 27;
        map.put("A", 1);
        map.put("B", 2);
        map.put("C", 3);
        map.put("D", 4);
        map.put("E", 5);
        map.put("F", 6);
        map.put("G", 7);
        map.put("H", 8);
        map.put("I", 9);
        map.put("J", 10);
        map.put("K", 11);
        map.put("L", 12);
        map.put("M", 13);
        map.put("N", 14);
        map.put("O", 15);
        map.put("P", 16);
        map.put("Q", 17);
        map.put("R", 18);
        map.put("S", 19);
        map.put("T", 20);
        map.put("U", 21);
        map.put("V", 22);
        map.put("W", 23);
        map.put("X", 24);
        map.put("Y", 25);
        map.put("Z", 26);
        
        
        
        int start = 0;
        int end = 1;
        int num = -1;
        
        List<Integer> list = new ArrayList<>();
        while(true) {
            
            if(end > msg.length()) {
                list.add(num);
                break;
            }
            String tmp = msg.substring(start, end);
            
            // System.out.print(tmp+ " ");
            // if(map.containsKey(tmp)) System.out.println(map.get(tmp));
            // else System.out.println("없음!");
            
            if(map.containsKey(tmp)) {
                num = map.get(tmp);
                end++;
            } else {
                list.add(num);
                start = end - 1;
                num = -1;
                map.put(tmp, alpha++);
            }
        }
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
