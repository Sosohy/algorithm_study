def solution(players, callings):
    rank = {players[i] : i for i in range(len(players))}
    
    for i in callings:
        idx = rank[i]
        rank[i] -= 1
        rank[players[idx-1]] += 1
        
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    return players

# 시간 초과 코드
# def solution(players, callings):
#     for i in callings:
#         idx = players.index(i)
#         players[idx] = players[idx-1]
#         players[idx-1] = i
        
#     return players