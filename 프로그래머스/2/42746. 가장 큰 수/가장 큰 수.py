def solution(numbers):
    if(sum(numbers) == 0): return '0'
    answer = ''
    numbersList = [str(i) for i in numbers]
    n = []
    
    for i in numbersList:
        n.append(i*3)
    n.sort(reverse=True)
    
    for i in n:
        tmp = len(i)//3
        answer += i[:tmp]
    
    return answer