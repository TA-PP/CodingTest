"""
문제 설명
선분 3개가 평행하게 놓여 있습니다. 
세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(lines):
    answer = 0
    num = {0 : 0, 1 : 0, 2 : 1, 3 : 1}
    temp = [0] * 201
    
    for i in range(3):
        mini = lines[i][0] + 100
        maxi = lines[i][1] + 100
        
        for i in range(mini, maxi):
            temp[i] += 1
            
    for i in range(len(temp)-1):
        if num[temp[i]] == 1:
            answer += 1
    return answer 