def solution(numbers, hand):
    keypad = {1:(0,0),2:(0,1),3:(0,2),
              4:(1,0),5:(1,1),6:(1,2),
              7:(2,0),8:(2,1),9:(2,2),
              '*':(3,0),0:(3,1),'#':(3,2)}
    
    leftH = '*'
    rightH = '#'
    answer = ''
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            leftH = i
        elif i in [3, 6, 9]:
            answer += 'R'
            rightH = i
        else:
            nextPos = keypad[i]
            lDist = abs(nextPos[0]-keypad[leftH][0]) + abs(nextPos[1]-keypad[leftH][1])
            rDist = abs(nextPos[0]-keypad[rightH][0]) + abs(nextPos[1]-keypad[rightH][1])
            
            if lDist < rDist:
                answer += 'L'
                leftH = i
            elif lDist > rDist:
                answer += 'R'
                rightH = i
            else:
                if hand == 'left':
                    answer += 'L'
                    leftH = i
                else:
                    answer += 'R'
                    rightH = i
    
    return answer