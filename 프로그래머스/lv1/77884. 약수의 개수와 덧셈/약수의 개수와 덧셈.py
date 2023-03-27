def isDivisorEven(x):
    div = 0
    for i in range(1, x+1):
        if x % i == 0:
            div += 1
    
    return (True if div%2 == 0 else False)
            
def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        isEven = isDivisorEven(i)

        if isEven:
            answer += i
        else:
            answer -= i
    
    return answer