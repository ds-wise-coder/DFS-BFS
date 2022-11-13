from collections import deque
N,M,K,X = map(int, input().split(' '))

visited=[False]*N
graph = [[] for _ in range(N+1)]

for i in range(M):
    x,y= map(int, input().split())
    graph[x].append(y)

#모든 도시에 대한 최단거리 초기화
dis = [-1]*(N+1) #방문하지 않은 도시 -1
dis[X]=0 #출발 도시는 0으로 설정

#BFS을 위해 deque()를 사용
q = deque()
q.append(X)

#queue가 빌때 까지 반복
while q:
    now = q.popleft() #now에는 1이 담기고 q는 비워짐
    
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next in graph[now]:
        # 아직 방문하지 않은 도시라면
        if dis[next]==-1:
            #최단거리 갱신
            #현재도시와 출발 도시 사이의 거리 + 1
            dis[next] = dis[now] + 1
            q.append(next)

#출발도시로부터 최단거리가 k인 도시가 존재하지 않는다면
#-1을 출력하기 위해 check변수를 False로 초기화 
check = False

for i in range(1,N+1):
    #도시간에 최단거리를 확인하여 K와 동일하면 그 도시를 출력
    if dis[i] == K:
        print(i)
        #최단거리가 K인 도시가 존재한다면 check를 True로 바꿔줌
        # -1이 출력되지 않도록 함
        check = True

#만약 최단거리가 k인 도시가 없다면 -1
if check == False:
    print(-1)



