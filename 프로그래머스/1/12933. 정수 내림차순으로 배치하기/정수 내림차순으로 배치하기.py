def solution(n):
    answer = 0
    
    n = list(str(n))
    n.sort(reverse=True)
    n = ''.join(n)
    
    return int(n)