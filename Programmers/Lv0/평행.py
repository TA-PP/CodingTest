"""
문제 설명
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
"""


from fractions import Fraction

def solution(dots):
    arr = []
    answer = 0
    
    for i in range(4):
        for j in range(i+1, 4):    
            x = dots[i][0] - dots[j][0]
            y = dots[i][1] - dots[j][1]
        
            fraction = Fraction(x, y)    
            
            if fraction in arr:
                answer = 1
            else:
                 answer = 0
                    
            arr.append(fraction)
            
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == 0:
                answer = 1
           
    return answer