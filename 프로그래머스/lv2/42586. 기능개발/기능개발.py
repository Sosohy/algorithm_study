import math
def solution(progresses, speeds):
    answer = []
    day = math.ceil((100-progresses[0])/speeds[0])
    done = 0
    
    while(progresses):
        work = progresses[0] + (speeds[0]*day)
        if(work >= 100):
            done += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            answer.append(done)
            day = math.ceil((100-progresses[0])/speeds[0])
            done = 0
    answer.append(done)

    return answer

'''
def solution(progresses, speeds):
    answer = []
    
    while(progresses):
        day = (100-progresses[0])//speeds[0]
        done = 0
        
        while(progresses):
            if(progresses[0] + (speeds[0]*day) >= 100):
                done += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break;
                
        answer.append(done)

    return answer
    
    
    
    def solution(progresses, speeds):
    answer = []
    day = (100-progresses[0])//speeds[0]
    done = 0
    
    while(progresses):
        if(progresses[0] + (speeds[0]*day) >= 100):
            done += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            answer.append(done)
            day = (100-progresses[0])//speeds[0]
            done = 0
    answer.append(done)

    return answer
'''