def solution(score):
    answer = []
    aver = []
    
    for i in score:
        aver.append((i[0]+i[1])/2)
    
    sort = sorted(aver, reverse=True)
    for i in aver:
        answer.append(sort.index(i)+1)
        
    return answer