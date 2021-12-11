from itertools import combinations

n = int(input())
data = []
teachers = []
spaces = []

for i in range(n):
    data.append(input().split())
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i, j))
        if data[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, direction):
    # 위쪽
    if direction == 0:
        while x >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽
    if direction == 1:
        while x < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1

    # 왼쪽
    if direction == 2:
        while y >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y -= 1

    # 오른쪽
    if direction == 3:
        while y < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y += 1

    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

flag = False

for obs in combinations(spaces, 3):
    for x, y in obs:
        data[x][y] = 'O'

    if not process():
        flag = True
        break

    for x, y in obs:
        data[x][y] = 'X'

if flag:
    print('YES')
else:
    print('NO')
