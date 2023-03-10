"""
문제 설명

소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
따라서 12의 소인수는 2와 3입니다. 
자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
"""
# 내가 풀은 코드
import math

def solution(n):
    temp = []
    answer = []
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            temp.append(i)
    print(temp)
    
    if len(temp) == 0:
        answer.append(n)
    return answer

-----------------------------------------------
# 다른 사람의 풀이
import math

def solution(n):
    answer = []
    
    for i in range(2, n+1):
        if n % i == 0:
            while(n % i == 0):
                n = n // i
            answer.append(i)
    return answer