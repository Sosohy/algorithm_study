def solution(bandage, health, attacks):
    answer = 0
    skillT, time = 0, 0
    char = health
    attack = attacks.pop(0)
    
    while(char > 0):
        time += 1
        
        if attack[0] == time:
            skillT = 0
            char -= attack[1]
            if attacks:
                attack = attacks.pop(0)
            else:
                if(char <= 0):
                    return -1
                return char
            continue
        
        skillT += 1
        if skillT == bandage[0]:
            char += bandage[2]
            skillT = 0
        char = min(char+bandage[1], health)
    
    return -1