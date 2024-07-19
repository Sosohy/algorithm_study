def solution(order):
    answer = 0
    asBelt = []
    idx = 0
    
    for i in range(1, len(order) + 1):
        asBelt.append(i)
        while (asBelt and asBelt[-1] == order[idx]):
            asBelt.pop()
            answer += 1
            idx += 1

    return answer
