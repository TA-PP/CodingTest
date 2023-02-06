from math import factorial

def solution(n):
    i = 1
    answer = 0
    while(True):
        if factorial(i) > n:
            answer = i - 1
            break
        i+=1
    return answer
