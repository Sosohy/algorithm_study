def solution(players, callings):
    answer = []
    rank = {players[i] : i for i in range(len(players))}
    
    for i in callings:
        idx = rank[i]
        rank[players[idx-1]] += 1
        rank[i] -= 1
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players