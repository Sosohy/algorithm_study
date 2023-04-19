def solution(skill, skill_trees):
    answer = 0
    
    for skillTree in skill_trees:
        isPossible = True
        skList = list(skill)
        
        for i in skillTree:
            if(i in skList):
                s = skList.pop(0)
                if(s != i):
                    isPossible = False
                    break
                if not skList:
                    break
                    
        if (isPossible):
            answer += 1
    
    return answer