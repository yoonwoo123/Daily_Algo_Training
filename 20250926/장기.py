# import sys
# from operator import countOf
#
# sys.stdin = open('장기.txt')
#
# N = int(input())
# if N == 3:
#     print(-1)
#     exit()

for N in range(90000, 95000):
    A = set()

    if N == 3:
        print(-1)
    if N % 2 == 0: # 짝수
        A.add(N//2)
        # print(N // 2)
        for i in range(1, N // 2):
            A.add(i)
            # print(i)
        for i in range(N // 2, N - 1):
            A.add(i + 2)
            # print(i + 2)
        A.add(N // 2 + 1)
        # print(N // 2 + 1)
    else:
        # print(N // 2 + 1)
        A.add(N // 2 + 1)
        for i in range(1, N // 2 + 1):
            # print(i)
            A.add(i)
        # print(N)
        A.add(N)
        for i in range(N // 2 + 2, N):
            # print(i)
            A.add(i)

    for i in range(2, N):
        if i == N // 2:
            if 1 not in A:
                print('1 없음')
                exit()
            if N not in A:
                print(f'{N} 없음')
                exit()
        if i not in A:
            print(f'{i} 없음')
            exit()

    # if len(A^B) != 0:
    #     print(len(A^B))
