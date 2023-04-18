def solution(x):
    answer = False
    x = str(x)
    
    num = sum(int(x[i]) for i in range(len(x))) 
    if(int(x)%num == 0):
        answer = True
    
    return answer