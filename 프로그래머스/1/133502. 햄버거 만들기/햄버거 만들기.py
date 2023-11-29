def solution(ingredient):
    answer = 0
    tmp = []
    recipe = [1, 2, 3, 1]
    
    for i in ingredient:
        tmp.append(i)
        if(tmp[-4:] == recipe):
            answer += 1
            for i in range(4):
                tmp.pop()
        
    return answer

'''
def solution(ingredient):
    answer = 0
    tmp = "".join(map(str, ingredient))
    recipe = "1231"

    while(recipe in tmp):
        tmp = tmp.replace(recipe,"", 1)
        answer += 1
        
    return answer
'''