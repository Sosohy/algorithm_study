def getBinary(x):
    binStr = ''
    
    while (x > 0): #3진법 구하고 리스트에 저장
        binStr += str(x%2)
        x = x//2
    
    return binStr

def solution(s):
    answer = [0, 0]
    
    while(s != '1'):
        answer[0] += 1
        answer[1] += s.count('0')
        s = getBinary(s.count('1'))

    return answer