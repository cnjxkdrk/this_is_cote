from collections import deque

n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # 레벨, 시간, x, y
            data.append((graph[i][j], 0, i, j))

data.sort()
target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque(data)

while queue:
    level, s, x, y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = level
                queue.append((level, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

# input 01
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2
#
# input 02
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2
