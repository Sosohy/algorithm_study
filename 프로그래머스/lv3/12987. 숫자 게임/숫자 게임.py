def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    while(A):
        aNum = A.pop()
        
        bNum = 0
        if(B[-1] > aNum):
            bNum = B.pop()
            answer += 1
        else:
            bNum = B.pop(0)
    
    return answer