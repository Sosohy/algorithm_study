from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    t1 = sum(queue1)
    t2 = sum(queue2)

    if (t1 + t2)%2 != 0: #홀수라 같을 수 없는 경우
        return -1
    elif t1 == t2: #이미 같은 경우
        return answer

    while answer < (len(queue1)*2)*2:
        if(t1>t2):
            tmp = q1.popleft()
            q2.append(tmp)
            t1 -= tmp
            t2 += tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            t2 -= tmp
            t1 += tmp

        answer += 1
        if(t1 == t2):
            return answer

    return -1