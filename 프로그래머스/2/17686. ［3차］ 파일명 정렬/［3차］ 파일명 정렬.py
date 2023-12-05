def solution(files):
    answer = []
    
    for f in files:
        head, num, tail = '', '', ''
        for i in range(len(f)):
            if(not head and f[i].isdigit()):
                head = f[:i]
                num = f[i:]

            if(head and not f[i].isdigit()):
                tail = f[i:]
                num = f[len(head):i]
                break

        answer.append((head, num, tail))
    
    answer.sort(key=lambda x:(x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in answer]
            
    return answer