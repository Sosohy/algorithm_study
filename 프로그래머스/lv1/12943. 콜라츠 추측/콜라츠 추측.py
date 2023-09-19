#DFS로 푼거
def DFS(i, num):
    if(500 < i):
        return -1
    elif(num == 1):
        return i
    else:
        if(num%2 == 0):
            return DFS(i+1, num//2)
        else:
            return DFS(i+1, (num*3)+1)
    
def solution(num):
    answer = DFS(0, num)
    return answer

'''
#그냥 푼거
def solution(num):
    answer = 0
    
    while(num != 1):
        answer += 1
        if(answer > 500): return -1
    
        if(num%2 == 0): # 짝수
            num = num/2
        else:
            num = num*3 + 1
        
    return answer
'''