# 1~n번 까지의 도시와 m개의 단방향 도로가 존재
# 특정 도시 x로부터 출발해 도달할 수 있는 모든 도시 중 최단거리가 정확히 k인 모든 도시의 번호를 출력하는 프로그램 작성.

# 솔루션
# 모든 도로의 거리: 1 == 모든 간선의 비용: 1
# 그래프에서 모든 간선의 비용이 동일할 때는 너비 우선 탐색-> 간단히 해결

# 특정 도시 X를 시작점으로 BFS 수행
# 모든 도시까지의 최단 거리 계산 -> 최단 거리를 하나씩 확인-> K인 경우 해당 도시 번호 출력

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m , k, x = map(int, input().split())
graph = [[]for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b =map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance =[-1]*(n+1)
distance[x]=0 # 출발 도시까지의 거리: 0

# 너비 우선 탐색(bfs) 수행
q =deque([x])
while q:
    now =q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문 x
        if distance[next_node]==-1:
            # 최단 거리 갱신
            distance[next_node]=distance[now]+1
            q.append(next_node)
# 최단거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        check = True
# 만약 최단거리가 K인 도시가 없다면 -1 출력
if check==False:
    print(-1)

