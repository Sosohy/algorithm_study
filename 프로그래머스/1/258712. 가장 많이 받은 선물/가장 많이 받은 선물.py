def solution(friends, gifts):
    answer = 0
    history = { friend : {} for friend in friends}
    index = { friend : 0 for friend in friends}
    
    for gift in gifts:
        give , receive = gift.split(" ")
        if(receive not in history[give]):
            history[give][receive] = 0 
        
        # 주고 받은 횟수
        history[give][receive] += 1
        
        # 선물 지수 계산 
        index[give] += 1
        index[receive] -= 1
    
    # 받을 선물 계산
    present = {friend : 0 for friend in friends}
    for i in range(len(friends)):
        a = friends[i]
        for j in range(i+1, len(friends)):
            b = friends[j]
            
            # 서로 주고 받은 선물 개수 비교
            p1 = history[a][b] if b in history[a] else 0
            p2 = history[b][a] if a in history[b] else 0
            
            if(p1 > p2): 
                present[a] += 1
            elif(p1 < p2):
                present[b] += 1
            else: # 주고 받은 개수 같은 경우, 선물 지수 비교
                aIdx, bIdx = index[a], index[b]
                if(aIdx > bIdx): present[a] += 1
                elif(aIdx < bIdx): present[b] += 1
    
    answer = max(present.values())
    return answer