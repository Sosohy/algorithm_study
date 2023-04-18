def solution(n):
    answer = 0
    
    nList = sorted(list(str(n)), reverse = True)
    answer = int(''.join(nList))
    
    return answer