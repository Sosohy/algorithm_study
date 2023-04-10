def solution(N, stages):
    dic = {}
    reach = len(stages)
    
    for i in range(1, N+1):
        if reach == 0:
            dic[i] = 0
        else:
            unclear = stages.count(i)
            dic[i] = unclear/reach
            reach -= unclear
    
    answer = sorted(dic, key=lambda x: dic[x], reverse=True)
    
    return answer 