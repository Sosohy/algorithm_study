def solution(s):
    answer = 0
    sList = list(s)
    dic = {')' : '(', ']' : '[', '}' : '{'}
    
    for i in range(len(s)):
        stack = []
        isPair = True
        
        for j in sList:
            if(j in ['(', '[', '{']):
                stack.append(j)
            else:
                if (not stack) or (stack[-1] != dic[j]):
                    isPair = False
                    break
                else:
                    stack.pop()
                    
        if(not stack) and isPair:
            answer += 1
        sList.append(sList.pop(0))

    return answer