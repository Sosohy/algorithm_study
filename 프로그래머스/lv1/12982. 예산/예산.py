def solution(d, budget):
    d.sort();
    print(d);
    
    sum = 0;
    for i in range(0, len(d)):
        sum += d[i];

        if(sum > budget):
            return i;
        
    return len(d);