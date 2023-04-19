def solution(n, words):
    answer = [0, 0]
    
    for i in range(1, len(words)):
        word = words[i]
        
        if (words[i-1][-1] != word[0]) or (word in words[:(i-1)]):
            return [(i%n)+1, (i//n)+1]
            
    return answer