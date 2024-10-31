def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        tmp = arr[s:e+1]
        
        m = -1
        for i in tmp:
            if(i>k):
                if(m == -1):
                    m = i
                else:
                    m = min(m, i)
        
        answer.append(m)
    
    return answer