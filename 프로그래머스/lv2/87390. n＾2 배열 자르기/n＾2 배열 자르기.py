def solution(n, left, right):
    answer = []
    
    while(left <= right):
        lidx = left%n
        
        if(lidx < left//n):
            answer.append((left//n)+1)
        else:
            answer.append(lidx+1)
        left += 1
        
    #print(answer)
    
    return answer