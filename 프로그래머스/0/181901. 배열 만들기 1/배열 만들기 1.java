class Solution {
    public int[] solution(int n, int k) {
        int num = n/k;
        int[] answer = new int[num];
        
        for(int i=0; i<num; i++){
            answer[i] = k*(i+1);
        }
        
        return answer;
    }
}