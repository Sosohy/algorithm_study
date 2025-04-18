def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if(i == "("):
            stack.append(i)
        elif(i == ')'):
            if(len(stack) > 0):
                stack.pop()
            else:
                return False
    
    return len(stack) == 0