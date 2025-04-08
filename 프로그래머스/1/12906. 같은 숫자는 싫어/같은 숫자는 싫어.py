from collections import deque

def solution(arr):
    st = []
    
    for i in arr:
        if(len(st) > 0 and st[-1] == i):
            continue
        st.append(i)

    return st