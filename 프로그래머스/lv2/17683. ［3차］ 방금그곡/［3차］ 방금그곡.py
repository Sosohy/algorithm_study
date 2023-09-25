def solution(m, musicinfos):
    answer = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for i in musicinfos:
        start, fin, title, score = i.split(',')
        
        start = list(map(int, start.split(":")))
        fin = list(map(int, fin.split(":")))
        pt = (fin[0]-start[0])*60 + (fin[1]-start[1])
        
        score = score.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        finSc = score*(pt//len(score)) + score[:(pt%len(score))]
        
        if m in finSc and ((not answer) or (answer[1] < pt)):
            answer = (title, pt)
        
        #print(title, score, pt, finSc, answer)
    
    if not answer:
        return "(None)"
    
    return answer[0]