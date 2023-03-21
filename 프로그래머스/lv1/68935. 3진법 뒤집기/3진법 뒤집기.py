def getTernary(x):
    s = [];
    
    while (x != 0): #3진법 구하고 리스트에 저장
        s.append(x%3);
        x = x//3;
    
    if(x != 0): s.append(x);
    return s;
    
def solution(n):
    answer = 0;
    nTernary = getTernary(n);
    nTernary.reverse();
    
    for i in range(0, len(nTernary)):
        answer += (nTernary[i] * pow(3, i))
    
    return answer