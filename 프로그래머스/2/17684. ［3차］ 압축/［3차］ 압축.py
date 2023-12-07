def solution(msg):
    answer = []
    base = list("-ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    msg = list(msg.upper())
    
    while(msg):
        tmp = msg.pop(0)
        while(msg and base.count(tmp+msg[0])):
            tmp += msg.pop(0)
        answer.append(base.index(tmp))
        if(msg):
            base.append(tmp+msg[0])
    
    return answer