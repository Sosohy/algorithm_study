def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        tmp = []
        for a, b in zip(arr1[i], arr2[i]):
            tmp.append(a+b)
        answer.append(tmp)
        
    return answer