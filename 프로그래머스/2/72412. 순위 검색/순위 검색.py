from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    infoDic = {}
    
    for i in info:
        infoList = i.split(" ")
        infoK = infoList[:-1]
        infoV = infoList[-1]

        for j in range(len(infoK)+1):  # key 모든 조합
            for c in combinations(infoK, j):
                tmp = ''.join(c)
                if tmp in infoDic:
                    infoDic[tmp].append(int(infoV))
                else:
                    infoDic[tmp] = [int(infoV)]
                    
    for i in infoDic:
        infoDic[i].sort()
        
    for i in query:
        qList = i.replace(" and ", " ").replace("-", "").split(" ")
        qInfo = "".join(qList[:-1])
        qScore = int(qList[-1].replace(" ", ""))
        
        if qInfo in infoDic:
            scores = infoDic[qInfo]
            if scores: 
                idx = bisect_left(scores, int(qScore))
                answer.append(len(scores) - idx)
        else:
            answer.append(0)
            
    return answer

'''
#효율성 실패
def solution(info, query):
    answer = []
    infoList = []
    
    for i in info:
        infoList.append(i.split(" "))
    
    for i in query:
        i = i.replace(" and ", " ")
        q = i.split(" ")
        cnt = 0

        for j in infoList:
            s = True
            if(int(j[-1]) >= int(q[-1])):
                for k in range(len(j)-1):
                    if(q[k] != '-' and q[k] != j[k]):
                        s = False
                        break
            else:
                s = False
                
            if s:
                cnt += 1
        answer.append(cnt)
    
    return answer
'''