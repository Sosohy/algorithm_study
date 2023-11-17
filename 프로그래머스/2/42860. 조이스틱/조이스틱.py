def solution(name):
    answer = 0
    a = ord('A')
    z = ord('Z')
    cursor = len(name)
    
    for i in range(len(name)):
        answer += min((ord(name[i])-a), 1+(z-ord(name[i])))
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        cursor = min(cursor, 2*i + len(name)-next, i + 2*(len(name) - next))
        
    return answer+cursor