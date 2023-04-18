def solution(a, b):
    answer = 0
    
    if(a == b): return a

    first = a
    last = b
    if(b < a):
        first = b
        last = a
        
    for i in range(first, last+1):
        answer += i
        
    return answer