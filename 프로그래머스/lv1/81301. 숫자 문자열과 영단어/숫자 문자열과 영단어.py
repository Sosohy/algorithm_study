def solution(s):
    numWord = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    answer = ''
    word = ''
    
    for i in range(len(s)):
        if(s[i].isdigit()):
            answer += s[i]
        else:
            word += s[i]
            if(word in numWord):
                answer += str(numWord[word])
                word = ''

    return int(answer)