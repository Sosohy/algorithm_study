def solution(s):
    answer = ''
    lt = len(s)
    
    if(lt%2 == 0): # 짝수
        n = lt//2
        answer = s[n-1:n+1]
    else:
        answer = s[lt//2]
        
    return answer