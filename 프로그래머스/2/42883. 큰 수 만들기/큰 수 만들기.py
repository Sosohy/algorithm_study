def solution(number, k):
    save = []
    
    for i in number:
        if save:
            if(k > 0):
                while(save[-1] < int(i)):
                    save.pop()
                    k -= 1
                    if not save or k <= 0:
                        break
            save.append(int(i))
        else:
            save.append(int(i))
    
    if(k > 0):
        save = save[:-k]
    return ''.join(map(str, save))