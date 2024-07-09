def solution(s):
    before = []
    
    for i in s:
        if(len(before) == 0):
            before.append(i)
        elif(before[-1] == i):
            before.pop()
        else:
            before.append(i)
    
    if(len(before) == 0):
        return 1

    return 0

# 효율성 통과 X
# def solution(s):
#     idx = 0
    
#     while(idx < len(s)-1):
#         if(s[idx] == s[idx+1]):
#             s = s[:idx] + s[idx+2:]
#             idx = 0
#         else:
#             idx += 1
        
#     if len(s) == 0:
#         return 1
    
#     return 0