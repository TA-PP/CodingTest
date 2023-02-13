"""
문제 설명

덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(quiz):
    answer = []
    temp = []
    tempAns = 0
    
    for i in quiz:
        temp = i.split()
        tempAns = int(temp[0])
        print(tempAns)
        for j in range(len(temp)):
            if temp[j] == '+':
                tempAns += int(temp[j+1])
            elif temp[j] == '-':
                tempAns -= int(temp[j+1])
        if tempAns == int(temp[-1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer