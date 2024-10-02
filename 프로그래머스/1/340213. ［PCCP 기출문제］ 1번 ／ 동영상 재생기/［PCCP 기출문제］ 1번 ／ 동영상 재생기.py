def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    def changeMinToSec(time):
        mm, ss = map(int, time.split(":"))
        sec = mm*60 + ss

        return sec
    
    Tpos = changeMinToSec(pos)
    TVideoLen = changeMinToSec(video_len)
    TopStart = changeMinToSec(op_start)
    TopEnd = changeMinToSec(op_end)

    if(TopStart <= Tpos <= TopEnd):
        Tpos = TopEnd

    for i in commands:

        if(i == "prev"):
            Tpos = max(0, Tpos-10)
        elif(i == "next"):
            Tpos = min(Tpos+10, TVideoLen)

        if(TopStart <= Tpos <= TopEnd):
            Tpos = TopEnd
    
    answer = str(Tpos//60).zfill(2) + ":" + str(Tpos%60).zfill(2)

    return answer
