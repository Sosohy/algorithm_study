def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        time = schedules[i]//100*100 + ((schedules[i]+10)%100)//60*100 + ((schedules[i]+10)%100)%60
        print(((schedules[i]+10)%100)%60)
        day = startday-1
        
        answer += 1
        for j in timelogs[i]:
            if(day < 5 and j > time):
                answer -= 1
                break
            day = (day+1)%7
        
    return answer