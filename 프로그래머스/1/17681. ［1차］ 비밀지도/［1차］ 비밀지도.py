def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        a1 = str(bin(arr1[i])[2:]).rjust(n,'0')
        a2 = str(bin(arr2[i])[2:]).rjust(n,'0')
        line = ''
        for j in range(n):
            if(a1[j] == '1' or a2[j] == '1'):
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer