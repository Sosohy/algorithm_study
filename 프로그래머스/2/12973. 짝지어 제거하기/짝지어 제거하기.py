def solution(s):
    answer = 0
    stack = []
    s = list(s)
    
    for i in range(len(s)):
        tmp = s[i]
        
        if(len(stack) <= 0):
            stack.append(tmp)
        else:
            if(stack[-1] == tmp):
                stack.pop()
            else:
                stack.append(tmp)
                
    if(len(stack) == 0):
        return 1

    return answer