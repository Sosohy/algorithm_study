def solution(n, left, right):
    answer = []
    
    while(left <= right):
        lidx = left%n
        
        if(lidx < left//n):
            answer.append((left//n)+1)
        else:
            answer.append(lidx+1)
        left += 1
        
        '''
        if(lidx < left//n):
            for i in range(lidx, (left//n)):
                answer.append((left//n)+1)
            left += (left//n)-lidx
        else:
            for i in range(lidx, n):
                answer.append(i+1)
            left += n-lidx
        '''
        
            
    #print(answer)
    
    return answer