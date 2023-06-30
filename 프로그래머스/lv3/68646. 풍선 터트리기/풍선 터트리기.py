def solution(a):
    answer = 0

    minLeft = []
    minRight = []
    minValue = a[0]
    
    for i in range(len(a)):
        minLeft.append(minValue)
        if a[i] < minValue:
            minValue = a[i]
    
    minValue = a[-1]
    for i in range(len(a)-1, -1, -1):
        minRight.append(minValue)
        
        if a[i] < minValue:
            minValue = a[i] 
    minRight.reverse()
        

    for i in range(len(a)):
        if (i == 0 or i == len(a)-1):
            answer += 1
        else:
            if(minLeft[i] > a[i] or minRight[i] >= a[i]):
                answer += 1

    return answer


'''
def solution(a):
    answer = 0
    
    for i in range(len(a)):
        if (i == 0 or i == len(a)-1):
            answer += 1
        else:
            n1Min = min(a[:i])
            n2Min = min(a[i+1:])
            
            if(n1Min > a[i] or n2Min > a[i]):
                answer += 1
            
    return answer
'''