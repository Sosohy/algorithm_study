def solution(numbers, direction):
    answer = []
    n = 1

    if(direction == "right"):
        numbers = numbers[-n:] + numbers[:-n]
    elif(direction == "left"):
        numbers = numbers[n:] + numbers[:n]

    return numbers