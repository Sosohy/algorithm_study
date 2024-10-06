def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    diceSet = list(set(dice))
    d  = len(diceSet)
    
    if(d == 1):
        answer = 1111*dice[0]
    elif(d == 2):
        if(dice.count(diceSet[0]) == 2):
            answer = (diceSet[0] + diceSet[1]) * abs(diceSet[0] - diceSet[1])
        else:
            p = max(dice, key=dice.count)
            q = min(dice, key=dice.count)
            answer = (10*p + q)**2
    elif(d == 3):
        p = max(dice, key=dice.count)
        diceSet.remove(p)
        answer = diceSet[0]*diceSet[1]
    else:
        answer = min(dice)
    
    return answer