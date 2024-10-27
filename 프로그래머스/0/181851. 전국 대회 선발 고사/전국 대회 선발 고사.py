def solution(rank, attendance):
    answer = 0
    aList = []
    
    while(len(aList) < 3):
        m = rank.index(min(rank))
        if(attendance[m]):
            aList.append(m)
        
        rank[m] += 100
    
    answer = (10000*aList[0]) + (100*aList[1]) + aList[2]
        
    return answer