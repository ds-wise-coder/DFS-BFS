from itertools import combinations
from collections import deque

N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

virus = deque() #바이러스 좌표 덱
block = deque() #벽 좌표의 덱
point = [] #벽을 놓을 수 있는 좌표

#벽 3개의 좌표 조합 생성
#바이러스 위치 확인
#벽 위치 확인
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            virus.append([i, j])
        elif matrix[i][j] == 1:
            block.append([i, j])
        else:
            point.append([i,j])

answer = 0
di = [1,-1,0,0]
dj = [0,0,1,-1]

for p in combinations(point, 3): #리스트에 있는 값들의 모든 조합 구하기
    #각 점을 벽으로 만들기
    one, two, three = p
    matrix[one[0]][two[1]] = 1
    matrix[two[0]][three[1]] = 1
    matrix[three[0]][one[1]] = 1

    visit = [[False]*M for _ in range(N)]
    for v in virus:
        visit[v[0]][v[1]] = True

    # 바이러스 전파
    q = virus.copy()
    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + dj[d]
            nj = j + dj[d]

            if ni < 0 or ni >= N or nj >= M: continue

            if matrix[ni][nj] == 0 and visit[ni][nj] == False:
                visit[ni][nj] = True
                q.append([ni,nj])

    safeArea = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0 and visit[i][j] == False :
                #벽이 놓여있고, 방문하지 않았다면
                # 바이러스가 퍼지지 않은 것
                safeArea +=1

    answer =max(answer,safeArea)
    # 벽으로 만든 부분 다시 돌려놓기
    matrix[one[0]][one[1]] = 0
    matrix[two[0]][two[1]] = 0
    matrix[three[0]][three[1]] = 0

print(answer)



