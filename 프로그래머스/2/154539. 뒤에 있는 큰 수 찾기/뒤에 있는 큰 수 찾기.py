def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer


# def solution(numbers):
#     answer = []

#     for i in range(len(numbers)):
#         num = numbers[i]
#         nextNum = -1
#         for j in range(i+1, len(numbers)):
#             if(num < numbers[j]):
#                 nextNum = numbers[j]
#                 break
#         answer.append(nextNum)
    
#     return answer
