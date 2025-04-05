def solution(x):
    answer = True
    
    l = sum(list(map(int, str(x))))
    if(x%l != 0):
        answer = False
    
    
    return answer