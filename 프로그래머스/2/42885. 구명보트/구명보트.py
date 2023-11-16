def solution(people, limit):
    people = sorted(people, reverse=True)
    small = len(people)-1
    answer = 0

    for i in range(len(people)):
        if i > small:
            break
        
        if people[i]+people[small]>limit: answer += 1
        else:
            small -= 1
            answer += 1

    return answer