from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    
    idList = list(permutations(user_id, len(banned_id)))
    
    def isMatch(uList):
        for m in range(len(banned_id)):
            uid, bid = uList[m], banned_id[m]
            if len(uid) != len(bid):
                return False

            for k in range(len(bid)):
                if(bid[k] != '*' and uid[k] != bid[k]):
                    return False
        return True
    
    for i in idList:
        if(isMatch(i)):
            u = list(set(i))
            if(u not in answer):
                answer.append(u)
    
    return len(answer)