import java.util.HashMap;

class Solution {
    public int solution(int n, String control) {
        int answer = n;
        
        HashMap<Character, Integer> num = new HashMap<>();
        num.put('w', 1);
        num.put('s', -1);
        num.put('d', 10);
        num.put('a', -10);
        
        for(int i=0; i<control.length(); i++){
            answer += num.get(control.charAt(i));
        }
        
        return answer;
    }
}