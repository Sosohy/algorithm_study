def solution(priorities, location):
    i = 0
    maxP = max(priorities)
    finish = 0
    
    while finish <= len(priorities):
        while True:
            if priorities[i] == maxP:
                if i == location:
                    return finish + 1
                break
            else:
                i = (i+1) % len(priorities)

        finish += 1
        priorities[i] = -1
        maxP = max(priorities)

    return len(priorities)