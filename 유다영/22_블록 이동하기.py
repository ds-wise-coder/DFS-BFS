'''
로봇개발자 무지는 한 달 앞으로 다가온 카카오배 로봇경진대회에 출품할 로봇을 준비하고 있습니다. 준비 중인 로봇은 2 x 1 크기의 로봇으로 무지는 0과 1로 이루어진 N x N 크기의 지도에서 2 x 1 크기인 로봇을 움직여 (N, N) 위치까지 이동 할 수 있도록 프로그래밍을 하려고 합니다. 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된 숫자 0은 빈칸을 1은 벽을 나타냅니다. 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다. 로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작하며, 앞뒤 구분없이 움직일 수 있습니다.
로봇이 움직일 때는 현재 놓여있는 상태를 유지하면서 이동합니다. 예를 들어, 위 그림에서 오른쪽으로 한 칸 이동한다면 (1, 2), (1, 3) 두 칸을 차지하게 되며, 아래로 이동한다면 (2, 1), (2, 2) 두 칸을 차지하게 됩니다. 로봇이 차지하는 두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 됩니다.
로봇은 다음과 같이 조건에 따라 회전이 가능합니다. 위 그림과 같이 로봇은 90도씩 회전할 수 있습니다. 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다. 로봇이 한 칸 이동하거나 90도 회전하는 데는 걸리는 시간은 정확히 1초 입니다. 0과 1로 이루어진 지도인 board가 주어질 때, 로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간을 return 하도록 solution 함수를 완성해주세요.

이 문제는 다소 복잡해 보이지만, 전형적인 BFS 문제 유형이다. 문제에서 로봇이 존재할 수 있는 각
위치(각 칸)를 노드로 보고, 인접한 위치와 비용이 1인 간선으로 연결되어 있다고 볼 수 있다. 간선의
비용이 모두 1로 동일하기 때문에 BFS를 이용하여 최적의 해를 구할 수 있다. 다시 말해 이 문제는
(1, 1)의 위치에 존재하는 로봇을 (N, N)의 위치로 옮기는 최단 거리를 계산하는 문제로 볼 수 있다.
다만, 이 문제가 일반적인 BFS 문제와 다른 점은, 로봇이 차지하고 있는 위치가 두 칸이며 최전을
통해 이동할 수 있다는 점이다. 물론 로봇이 차지하고 있는 위치가 두 칸이라고 해도, 여전히 방문
여부를 관리할 수 있으니 걱정하지 말자. 바로 위치 정보를 튜플로 처리하면 된다. 로봇의 상태를
집합 자료형으로 관리한다고 가정홰보자. 로봇의 상태를 집합 자료형을 이용하여 관리하면, 한 번
방문한(큐에 들어간) 자전거의 상태는 두 번 방문하지 않는다. 먼저 로봇이 단순하게 이동하는 경우는
단순이 상, 하, 좌, 우로 이동하는 모든 경우를 계산하면 된다. 회전의 경우 로봇이 가로로 놓여 있는 경우와 세로로 놓여 있는 경우를 모두 고려해야 한다.가로로 놓은 상태에서 아래쪽, 위쪽으로 회전하는 경우 혹은 세로로 놓인 상태에서 오른쪽, 왼쪽으로 회전하는 경우. 또한 소스코드를 간단하게 작성하기 위하여, 초기에 주어진 맵을 변형하여 외곽에 벽을 둘 수 있다. 이렇게 하면 로봇이 맵을 벗어나지 않는지, 그 범위 판정을 더 간단히 할 수 있다.
'''
# https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3#

from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 반환 결과 (이동 가능한 위치들)
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + \
                                                             dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:  # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:  # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}  # 시작 위치 설정
    q.append((pos, 0))  # 큐에 삽입한 뒤에
    visited.append(pos)  # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
