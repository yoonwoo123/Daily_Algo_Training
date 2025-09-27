import sys
sys.stdin = open('토마토2.txt')

import collections
def BFS(starts):
    global ans
    que = collections.deque(starts)

    while que:
        z, x, y, time = que.popleft()
        for dx, dy, dz in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H or arr[nz][nx][ny] < 0: continue
            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = time + 1
                que.append([nz, nx, ny, time + 1])
        ans = time - 1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = 0
startPos = []

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                startPos.append([k, i, j, 1])

BFS(startPos)

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                ans = -1
                break
        if ans == -1:
            break
    if ans == -1:
        break

print(ans)
