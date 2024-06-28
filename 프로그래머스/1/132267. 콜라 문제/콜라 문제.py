def solution(a, b, n):
    answer = 0
    
    while(n >= a):
        newCola = (n//a) * b
        answer += newCola
        n = n%a + newCola
    
    return answer