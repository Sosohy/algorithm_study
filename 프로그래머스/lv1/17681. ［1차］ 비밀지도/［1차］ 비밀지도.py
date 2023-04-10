def getBinary(n, num):
    binary = ''
    
    while(num>0):
        binary += str(num%2)
        num = num//2
        
    while(len(binary) < n):
        binary += '0'
        
    return binary[::-1]
        

def solution(n, arr1, arr2):
    trMap = [[' ' for j in range(n)] for i in range(n)]
    
    for i in range(n):
        ar1 = getBinary(n, arr1[i])
        ar2 = getBinary(n, arr2[i])
        for j in range(n):
            if(ar1[j] == '1' or ar2[j] == '1'):
                trMap[i][j] = '#'
    
    answer = []
    for i in trMap:
        answer.append(''.join(map(str, i)))
        
    return answer