def solution(board, moves):
    answer = 0
    stack = []
    
    for i in moves:
        i -= 1

        for j in board:
            if(j[i] != 0):
                if(len(stack) > 0 and stack[-1] == j[i]):
                    stack.pop()
                    answer += 2
                else:
                    stack.append(j[i])
                j[i] = 0
                break;
    
    return answer