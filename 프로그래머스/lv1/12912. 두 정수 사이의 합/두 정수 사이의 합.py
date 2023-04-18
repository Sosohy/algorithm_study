def solution(a, b):
    answer = 0
    
    if(a == b): return a

    if(b < a):
        a, b = b, a
        
    return sum(range(a,b+1))