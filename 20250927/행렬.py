import sys
sys.stdin = open('행렬.txt')

def reverse(i, j):
    for r in range(i, i + 3):
        for c in range(j, j + 3):
            A[r][c] ^= 1

ans = 0
N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

for x in range(N - 2):
    for y in range(M - 2):
        if A[x][y] != B[x][y]:
            reverse(x, y)
            ans += 1

print(ans if A == B else -1)

