def solution(today, terms, privacies):
    answer = [];
    
    todaySplit = today.split('.');
    nowDays = int(todaySplit[0])*12*28 + int(todaySplit[1])*28 + int(todaySplit[2]);
    #print(nowDays);
    
    dicTerms = {}
    for i in terms:
        term = i.split(' ');
        dicTerms[term[0]] = int(term[1])*28;
        #print(dicTerms[term[0]])
    
    p = 1;
    for i in privacies:
        pString = i.split(' ')[0].split('.');
        term = dicTerms[i.split(' ')[1]]
        exDays = int(pString[0])*12*28 + int(pString[1])*28 + int(pString[2]) + term;
        
        if (exDays <= nowDays):
            answer.append(p);
        p += 1;
    
    return answer