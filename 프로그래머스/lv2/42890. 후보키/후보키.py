from itertools import combinations 

def solution(relation):
    comList = []
    for i in range(1,len(relation[0])+1):
        comList.extend(combinations(range(len(relation[0])),i))
    
    #유일성 
    unique = []
    for i in comList :
        tmp = [tuple(item[key] for key in i) for item in relation]
        if len(set(tmp)) == len(relation) :
            unique.append(i)
            
    # 최소성 
    answer = set(unique)
    for i in range(len(unique)) :
        for j in range(i+1, len(unique)) :
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])) :
                answer.discard(unique[j])
    return len(answer)