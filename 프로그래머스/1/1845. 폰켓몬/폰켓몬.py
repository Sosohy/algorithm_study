def solution(nums):
    answer = 0
    t = len(set(nums))
    
    answer = min(t, len(nums)//2)
    
    return answer