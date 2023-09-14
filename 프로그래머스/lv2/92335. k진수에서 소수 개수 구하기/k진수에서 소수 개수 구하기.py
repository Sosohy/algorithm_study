import math
def solution(n, k):
    answer = 0
    num = ''

    while(n>0):
        num += str(n%k)
        n //= k
    
    num = num[::-1]
    spList = num.split('0')

    for i in spList:
        if(i != '' and isPrime(int(i))):
            answer += 1
        
    return answer

def isPrime(n):
    if(n > 1):
        for i in range(2, int(math.sqrt(n))+1):
            if(n%i == 0):
                return False 
        else:
            return True
    return False