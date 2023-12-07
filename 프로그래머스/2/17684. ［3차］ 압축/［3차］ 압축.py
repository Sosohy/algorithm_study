def solution(msg):
    answer = []
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = {k:v for (k, v) in zip(a, list(range(1, 27)))}
    msg = list(msg)
    idx = len(a)+1
    
    while(msg):
        tmp = msg.pop(0)
        while(msg and base.get(tmp+msg[0], 0)):
            tmp += msg.pop(0)
        answer.append(base.get(tmp))
        if(msg):
            base[tmp+msg[0]] = idx
            idx += 1
    
    return answer


'''
def solution(msg):
    answer = []
    base = list("-ABCDEFGHIJKLMNOPQRSTUVWXYZ") # dict()으로 만들어서 풀어도 O
    msg = list(msg)
    
    while(msg):
        tmp = msg.pop(0)
        while(msg and base.count(tmp+msg[0])):
            tmp += msg.pop(0)
        answer.append(base.index(tmp))
        if(msg):
            base.append(tmp+msg[0])
    
    return answer
'''