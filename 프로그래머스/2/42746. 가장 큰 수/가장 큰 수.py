def solution(numbers):
    if(sum(numbers) == 0): return '0'
    answer = ''
    nList = [str(i) for i in numbers]
    
    for i in range(len(nList)):
        nList[i] = nList[i]*3
    nList.sort(reverse=True)
    
    for i in nList:
        tmp = len(i)//3
        answer += i[:tmp]
    
    return answer