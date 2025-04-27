import math
def solution(progresses, speeds):
    answer = []
    day = math.ceil((100-progresses[0])/speeds[0])
    done = 0
    
    for i in range(len(progresses)):
        now = progresses[i] + speeds[i]*day
        
        if(now >= 100):
            done += 1
        else:
            answer.append(done)
            day = math.ceil((100-progresses[i])/speeds[i])
            done = 1
            
#     while(progresses):
#         now = progresses[0] + speeds[0]*day
        
#         if(now >= 100):
#             done += 1
#             progresses.pop(0)
#             speeds.pop(0)
#         else:
#             answer.append(done)
#             day = math.ceil((100-progresses[0])/speeds[0])
#             done = 0
    
    answer.append(done)
    
    return answer