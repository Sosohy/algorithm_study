from collections import deque

def solution(priorities, location):
    priorities = list(zip(priorities, range(len(priorities))))
    
    process = priorities[location]
    q = deque(priorities)
    cnt = 0
    
    while q:
        m_idx = 0

        for i in range(len(q)):
            if q[m_idx][0] < q[i][0]: m_idx = i
            
        print(q, m_idx, q[m_idx])

        if q[m_idx][1] == process[1]:
            if q[m_idx][1]!=location: cnt += q.index(process)
            return cnt + 1

        for j in range(m_idx):
            q.append(q.popleft())

        p = q.popleft()
        cnt += 1

    return cnt