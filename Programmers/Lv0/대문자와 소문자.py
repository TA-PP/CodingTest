"""
문제 설명

문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_string):
    answer = ''
    temp = 0
    
    for i in my_string:
        temp = ord(i)
        if ord(i) >= 65 and ord(i) <= 90:
            temp += 32
            answer += chr(temp)
        else:
            temp -= 32
            answer += chr(temp)
    return answer