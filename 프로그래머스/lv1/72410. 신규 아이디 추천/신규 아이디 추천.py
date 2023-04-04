def solution(new_id):
    spLetter = ['-', '_', '.']
    new_id = new_id.lower() # 1 : 소문자 치환
    answer = ''
    
    # 2: 문자 제거
    for i in new_id:
        if (i.isalpha() or i.isdigit()) or (i in spLetter):
            answer += i
    
    # 3 : 연속 . 치환
    while('..' in answer):
        answer = answer.replace('..', '.')
    
    # 4 : 처음과 끝 마침표 제거
    answer = answer.strip('.')
    
    # 5 : 빈 문자열 a 대입
    if (len(answer) == 0):
        answer += 'a'
    
    # 6 : 16자 이상 처리
    if (len(answer) > 15):
        answer = answer[0:15].rstrip('.')
        
    # 7 : 2자 이하 -> 길이 3
    while(len(answer) < 3):
        answer += answer[-1]
        
    print(answer)

    return answer