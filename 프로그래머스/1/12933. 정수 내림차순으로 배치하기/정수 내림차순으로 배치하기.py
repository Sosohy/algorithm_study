def solution(n):
    answer = 0
    
    n = [i for i in str(n)]
    n.sort(reverse=True)
    n = ''.join(n)
    
    return int(n)