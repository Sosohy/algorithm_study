def solution(survey, choices):
    answer = ''
    dicType = {"R":0, "T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    for i in range(len(survey)):
        disagree = survey[i][0]
        agree = survey[i][1]
        
        j = choices[i]
        if(j <= 4): #비동의일 경우
            dicType[disagree] += 4 - j
        elif(4 < j): #동의일 경우
            dicType[agree] += j - 4
    
    values = list(dicType.values())
    keys = list(dicType.keys())
    print(values)
    for i in range(0, len(dicType), 2):
        m = max(values[i], values[i+1])
        if(dicType[keys[i]] == m):
            answer += keys[i]
        else:
            answer += keys[i+1]
    
    return answer