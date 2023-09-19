def DFS(dic, start):
    path = []
    stack = [start]
    
    while stack:
        now = stack[-1]
        
        if (now not in dic) or (len(dic[now]) == 0):
            path.append(stack.pop())
        else:
            stack.append(dic[now].pop(0))
            
    return path[::-1]
    
    
def solution(tickets):
    dic = {}
    
    for t in tickets:
        if t[0] not in dic:
            dic[t[0]] = [t[1]]
        else:
            dic[t[0]].append(t[1])
    
    for i in dic:
        dic[i].sort()
    
    answer = DFS(dic, "ICN")
    
    return answer