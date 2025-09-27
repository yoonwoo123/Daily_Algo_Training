import sys
sys.stdin = open('행렬.txt')

N, M = map(int, input().split())

A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

# print(A)
# print(B)

if M < 3:
    print(-1)
    exit(0)

