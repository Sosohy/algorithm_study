def solution(n, w, num):
    answer = 0
    x = 1
    h = n//w+1
    box = []
    
    for j in range(h):
        tmp = []
        for i in range(w):
            if(x <= n):
                tmp.append(x)
                x += 1
            else:
                tmp.append(0)
        if(j%2 == 0):
            box.append(tmp)
        else:
            box.append(tmp[::-1])
    
    for i in range(len(box)):
        for j in range(len(box[0])):
            if(box[i][j] == num):
                idx = i
                while(idx < h and box[idx][j] != 0):
                    answer += 1
                    idx += 1

    return answer