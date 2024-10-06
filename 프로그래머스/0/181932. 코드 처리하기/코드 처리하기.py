def solution(code):
    answer = ''
    mode = False
    
    for i in range(len(code)):
        if(code[i] == '1'):
            mode = not mode
        elif(mode == True and i%2 != 0):
            answer += code[i]
        elif(mode == False and i%2 == 0):
            answer += code[i]
        
    return "EMPTY" if len(answer) == 0 else answer