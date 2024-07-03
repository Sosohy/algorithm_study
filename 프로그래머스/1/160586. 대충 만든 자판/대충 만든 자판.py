def solution(keymap, targets):
    answer = []
    idxDic = {}
    
    for i in keymap:
        for j in range(len(i)):
            ch = i[j]
            if ch not in idxDic:
                idxDic[ch] = j+1
            else:
                idxDic[ch] = min(idxDic[ch], j+1)
    
    for i in range(len(targets)):
        cnt = 0
        for j in range(len(targets[i])):
            if(targets[i][j] in idxDic):
                cnt += idxDic[targets[i][j]]
            else:
                cnt = -1
                break;
        answer.append(cnt)
    
    return answer