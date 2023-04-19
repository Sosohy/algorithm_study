def solution(sizes):
    answer = 0
    w = []
    h = []
    
    for i in sizes:
        w.append(min(i))
        h.append(max(i))
        
    answer = max(w) * max(h)
        
    return answer