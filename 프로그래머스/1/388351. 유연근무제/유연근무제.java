class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        
        for(int i=0; i<schedules.length; i++){
            int time = ((schedules[i]+10)/100 + ((schedules[i]+10)%100)/60)*100 // 시
                       + ((schedules[i]+10)%100)%60; // 분
            
            int cnt = 0;
            for(int j=0; j<timelogs[0].length; j++){
                int log = timelogs[i][j];
                boolean isWeek = ((startday+j)%7 > 0 && (startday+j)%7 < 6);
                
                if(isWeek && log <= time){
                    cnt += 1;
                }
            }
            if(cnt >= 5){
                answer += 1;
            }
            
        }
        
        
        return answer;
    }
}