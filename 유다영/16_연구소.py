# 전체 맵: 8x8, 벽 설치할 수 있는 모든 조합의 수 == 최악의 경우 64C3
# 조합 계산 -> 파이썬 조합 라이브러리 이용, DFS, BFS 이용해 해결 가능
# 벽의 개수가 3개가 되는 모든 조합을 찾은 후 조합에 대한 안전 크기 계산

n, m = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 벽 설치한 후 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split)))

# 4가지 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0


# 깊이 우선 탐색(dfs) -> 각 바이러스가 사방으로 퍼짐
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 중 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치, 다시 재귀수행
                temp[nx][ny] = 2
                virus(nx, ny)


# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
