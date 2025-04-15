def solution(s):
    answer = ''
    sList = list(map(int, s.split()))
    
    return str(min(sList)) + " " + str(max(sList))