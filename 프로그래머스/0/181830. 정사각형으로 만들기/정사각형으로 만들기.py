def solution(arr):
    r = len(arr)
    c = len(arr[0])
    
    if(r>c):
        for i in range(r):
            for j in range(r-c):
                arr[i].append(0)
    elif(r<c):
        for i in range(c-r):
            tmp = [0]*c
            arr.append(tmp)

    return arr