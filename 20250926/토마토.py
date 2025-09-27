import sys
sys.stdin = open('토마토.txt')

import collections
def BFS(starts):
    global ans
    que = collections.deque(starts)

    while que:
        x, y, time = que.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or arr[nx][ny] < 0: continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = time+1
                que.append([nx, ny, time + 1])
        ans = time - 1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
startPos = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            startPos.append([i, j, 1])

BFS(startPos)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            ans = -1
            break
    if ans == -1:
        break

print(ans)
