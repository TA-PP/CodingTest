'''
문제 설명
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 
solution 함수를 완성해주세요.
'''

def solution(numlist, n):
    answer = []
    subnum = [[]]
    temp = []
    
    numlist.sort()
    
    for i in numlist:
        temp.append(i)
        temp.append(abs(i-n))
        subnum.append(temp)
        temp = []
    
    subnum.pop(0)
    
    for i in range(len(subnum)-1):
        for j in range(i+1, len(subnum)):
            if subnum[i][1] > subnum[j][1]:
                temp = subnum[i]
                subnum[i] = subnum[j]
                subnum[j] = temp
                
    for i in range(len(subnum)-1):
        for j in range(i+1, len(subnum)):
            if subnum[i][1] == subnum[j][1]:
                temp = subnum[i]
                subnum[i] = subnum[j]
                subnum[j] = temp
    
    for i in subnum:
        answer.append(i[0])
        
    return answer