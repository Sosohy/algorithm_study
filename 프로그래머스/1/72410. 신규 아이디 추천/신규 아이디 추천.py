def solution(new_id):
    answer = ''
    ok = ['-', '_', '.']
    new = new_id.lower()

    for i in new:
        if(i.isdigit() or i.isalpha() or i in ok):
            answer += i
    
    while('..' in answer):
        answer = answer.replace('..', '.')

    answer = answer.strip('.')
    
    if(len(answer) == 0):
        answer += 'a'
    
    if(len(answer) > 15):
        answer = answer[:15]
        answer = answer.strip('.')
    
    while(len(answer) < 3):
        answer += answer[-1]
    
    return answer