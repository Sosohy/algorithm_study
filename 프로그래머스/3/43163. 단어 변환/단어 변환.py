from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    v = [0 for i in range(len(words))]
    
    while(q):
        w, cnt = q.popleft()
        if w == target:
            return cnt
        
        for i in range(len(words)):
            if v[i] == 0:
                tmp = 0
                for j in range(len(w)):
                    if(w[j] != words[i][j]):
                        tmp += 1
                
                if tmp == 1:
                    q.append((words[i], cnt+1))
                    v[i] = 1
    
    return answer