from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while(len(people) > 1):
        s = people.pop()
        if s+people[0] <= limit:
            s += people.popleft()
        answer += 1
        
    if(people):
        answer += 1
        
    return answer