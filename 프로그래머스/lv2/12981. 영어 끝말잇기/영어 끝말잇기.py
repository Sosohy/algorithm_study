import math

def solution(n, words):
    answer = []
    no_dup_words = []
    dup_n1 = 0
    
    
    # 같은 단어를 말했을 때
    for i, w in enumerate(words):
        if w not in no_dup_words:
            no_dup_words.append(w)
        else:
            dup_n1 = i+1
            break
    
    print(dup_n1)
            
    #맞지 않는 단어를 말했을 때
    dup_n2 = 0
    w_fir = ''
    w_end = words[0][0]
    
    for i, w in enumerate(words):
        w_fir = w[0]
        if w_fir != w_end:
            dup_n2 = i+1
            break
        w_end = w[-1]
    
    print(dup_n2)
    #if dup_n1 != 0 and dup_n2 != 0 and dup_n2 < dup_n1 : dup_n1 = dup_n2
    print(dup_n1)
    #print(math.ceil(dup_n1/n))
    #print(dup_n1%n if dup_n1%n != 0 else n )#탈락하는 사람의 번호
    #print(math.ceil(dup_n1/n)) #그사람의 순서
    
    if dup_n1 == 0 and dup_n2 == 0:
        return [0, 0]
    
    if dup_n2 == 0:
        answer.append(dup_n1%n if dup_n1%n != 0 else n)
        answer.append(math.ceil(dup_n1/n))
    elif dup_n1 == 0:
        answer.append(dup_n2%n if dup_n2%n != 0 else n)
        answer.append(math.ceil(dup_n2/n))
    else:
        m = min(dup_n2, dup_n1)
        answer.append(m%n if m%n != 0 else n)
        answer.append(math.ceil(m/n))
        
    return answer

'''
def solution(n, words):
    answer = [0, 0]
    
    for i in range(1, len(words)):
        word = words[i]
        
        if (words[i-1][-1] != word[0]) or (word in words[:(i-1)]):
            return [(i%n)+1, (i//n)+1]
            
    return answer
'''