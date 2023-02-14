"""
문제 설명

머쓱이는 RPG게임을 하고 있습니다. 
게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 
예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
"""

def solution(keyinput, board):
    xtemp = 0
    ytemp = 0
    dic = {'left':[-1, 0], 'right' : [1, 0], 'up' : [0, 1], 'down' : [0, -1]}
    
    for i in keyinput:
        xtemp += dic[i][0]
        ytemp += dic[i][1]        
        
        if abs(xtemp) > (board[0] // 2):  
            if xtemp == 1:
                xtmep = 1
            elif xtemp > 0:
                xtemp = board[0] // 2
            elif xtemp < 0:
                xtemp = -(board[0] // 2)
        elif abs(ytemp) > (board[1] // 2):
            if ytemp == 1:
                ytemp = 1
            elif ytemp > 0:
                ytemp = board[1] // 2
            elif ytemp < 0:
                ytemp = -(board[1] // 2)
            
    answer = [xtemp, ytemp]
    return answer