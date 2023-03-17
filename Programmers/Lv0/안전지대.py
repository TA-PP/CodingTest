'''
문제 설명
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
'''

def solution(board):
    index = []
    count = len(board) ** 2
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                count -= 1                        
    if count == 0:
        return 0
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                index.append([i-1, j-1])
                index.append([i-1, j])
                index.append([i-1, j+1])
                index.append([i, j-1])
                index.append([i, j+1])
                index.append([i+1, j-1])
                index.append([i+1, j])
                index.append([i+1, j+1])         
                
    for i in index:
        if i[0] >= 0 and i[1] >= 0:
            if i[0] < len(board) and i[1] < len(board):
                board[i[0]][i[1]] = 1
                
    count = len(board) ** 2
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                count -= 1
            
    return count