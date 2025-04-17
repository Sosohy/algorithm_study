def solution(n, words):
    turn = 0
    answer = [0, 0]
    stack = []
    
    for i in range(len(words)):
        word = words[i]
        if(len(stack) <= 0):
            stack.append(word)
        else:
            if(stack[-1][-1] != word[0] or (word in stack) or len(word) == 1):
                return [(i%n)+1, (i//n)+1]
            else:
                stack.append(word)
    
    return answer