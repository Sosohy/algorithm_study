def solution(s):
    answer = 0
    left = ""
    dic = {'(':')', '[':']', '{':'}'}
    
    def isCorrect(gStr):
        stack = []
        
        for i in range(len(gStr)):
            
            if(stack and stack[-1] in dic and gStr[i] == dic[stack[-1]]):
                stack.pop()
            else:
                stack.append(gStr[i])
        
        if(len(stack) == 0):
            return True
        
        return False
    
    for k in range(len(s)):
        left += s[k]
        
        if (isCorrect(s[k+1:]+left)):
            answer += 1
    
    return answer