import math

def solution(fees, records):
    answer = []
    dicIn = dict()
    outCars = dict()
    
    for i in records:
        time, carNum, typeR = i.split(" ");
        
        if typeR == "IN":
            dicIn[carNum] = time
        else: #OUT일 경우
            parkT = getTime(time) - getTime(dicIn[carNum])
            
            if carNum in outCars:
                outCars[carNum] += parkT
            else:
                outCars[carNum] = parkT
                
            dicIn.pop(carNum)
        
    for key in dicIn.keys():
        parkT = getTime("23:59") - getTime(dicIn[key])

        if key in outCars:
            outCars[key] += parkT
        else:
            outCars[key] = parkT 
    
    #요금 일괄 계산
    for key, value in sorted(outCars.items()):
        if value <= fees[0]:
            answer.append(fees[1])
        else:
            feeN = fees[1] + math.ceil((value - fees[0])/fees[2]) * fees[3]
            answer.append(feeN)
            
    return answer

def getTime(str):
    t = str.split(":")
    return int(t[0])*60 + int(t[1])