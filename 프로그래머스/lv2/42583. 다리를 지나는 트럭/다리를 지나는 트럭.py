def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    truckSum = 0
    
    while bridge:
        answer += 1
        truckSum -= bridge.pop(0)
        
        if truck_weights:
            if truckSum + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                truckSum += truck
            else:
                bridge.append(0)
                
    return answer


'''
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = []
    tmp = 0
    
    while truck_weights:
        if (sum(trucks) + truck_weights[0]) <= weight:
            if trucks:
                tmp += 1    
            trucks.append(truck_weights.pop(0))
        else:
            answer += (bridge_length + tmp)
            trucks.clear()
            tmp = 0
            
    answer += (bridge_length + tmp + 1)        
    
    return answer
'''