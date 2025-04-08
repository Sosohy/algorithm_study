def solution(genres, plays):
    answer = []
    gDic = {}
    pDic = {}
    
    for i in range(len(genres)):
        if(genres[i] not in gDic):
            gDic[genres[i]] = 0
            pDic[genres[i]] = []
        gDic[genres[i]] += plays[i]
        pDic[genres[i]].append((i, plays[i]))
    
    gList = sorted(gDic, key=lambda x:gDic[x], reverse=True)
    
    for i in gList:
        pList = sorted(pDic[i], key=lambda x:(-x[1], x[0]))
        for j in pList[:2]:
            answer.append(j[0])
    
    return answer