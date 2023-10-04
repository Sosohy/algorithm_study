def solution(enroll, referral, seller, amount):
    answer = {}
    refer = {}
    
    for i in range(len(enroll)):
        refer[enroll[i]] = referral[i]
        answer[enroll[i]] = 0
    
    for i in range(len(seller)):
        sList = []
        tmp = seller[i]
        profit = 100*amount[i]
        
        while (True):
            if(profit > 1):
                p = profit//10
                answer[tmp] += profit-p
                profit = p
                tmp = refer[tmp]
            else:
                answer[tmp] += profit
                break
                
            if(tmp == '-'):
                break
            
    return list(answer.values())
