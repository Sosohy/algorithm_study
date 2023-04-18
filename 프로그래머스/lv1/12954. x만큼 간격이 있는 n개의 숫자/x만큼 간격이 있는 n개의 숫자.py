def solution(x, n):
    answer = []
    
    for i in range(1, n+1):
        answer.append(x*i)
        
    """
    num = x
    
    while(len(answer)<n):
        answer.append(num)
        num += x 
    """
        
    return answer