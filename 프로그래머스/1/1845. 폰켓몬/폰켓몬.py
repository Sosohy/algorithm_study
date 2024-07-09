def solution(nums):
    
    typeList = set(nums)
    answer = min(len(typeList), len(nums)//2)
    
    return answer