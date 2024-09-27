class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        
        for(int i=0; i<num_list.length; i++){
            answer[i] = num_list[i];
        }
        
        int end = num_list[num_list.length - 1];
        int end2 = num_list[num_list.length - 2];
        if(end > end2){
            answer[answer.length - 1] = end - end2;
        }else{
            answer[answer.length - 1] = end*2;
        }
        
        return answer;
    }
}