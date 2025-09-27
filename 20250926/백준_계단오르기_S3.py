import sys
sys.stdin = open("백준_계단오르기_S3.txt")

'''
계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
'''


# 1계단 오르는 방법과 2계단 오르는 방법 2가지로 모든 경우의 수를 탐색해보자.
# 대신에 최대값을 구하는 것이기 때문에 DP 로 시간을 최소화 할 수 있는 방법도 고려하자 DFS
# 2계단씩 보면서 얻을 수 있는 최대값을 가져가는 식으로 짜면 어떨까?
# -> 그런데 계단은 최대한 많이 밟는 게 이득이므로 3계단 연속 룰을 지키면서 최대한 밟아야 한다.
# 그 말은 즉 2계단씩이 아닌 3계단 씩 봐야한다.
# 대신에 3계단 연속으로 밟을 수 없다는 룰을 지켜야 한다.

# 3번째 룰 때문에 마지막 계단부터 역순으로 시작하는게 편해보인다.
# 현재 계단을 기준으로 3,2 번째 계단과 3,1번째 계단의 합을 비교하면서 내려간다.
# 범위를 벗어난 계단에 도달하는 경우엔 계단의 값을 0으로 치자, 무조건 첫번째 계단이 들어간 합이 크게 나올 것이며
# 0번째 인덱스 (첫번째 계단)에 도달하는 순간의 값을 반환

# 3,2 과 3,1 비교 현재 pos가 5라면, 5-3 5-2의 값의 합과, 5-3 5-1의 값의 합을 비교
# 더 큰 값이 3,2라면 pos -= 2 해주고 tot에 2의 합을 더해줌, 3,1라면 pos -= 3 해주고 tot에 3,1의 합을 전부 더해줌
# 그런데 가정을 해보니 여기서, 동점이 되는 경우라면 두 개의 경우 모두 끌고 가야 한다는 것이다..
# 즉

# def sol():
#     if N < 3:
#         print(sum(stairs))
#         return
#     # lastPos, status : val
#     dp = {(0, 0): stairs[0], (1, 0): stairs[1], (1, 1): stairs[0] + stairs[1]}
#
#     for i in range(2, N):
#         dp[(i, 0)] = dp[(i - 2, 0)] + stairs[i]
#         dp[(i, 1)] = dp[(i - 1, 0)] + stairs[i]
#         dp[(i-1, 0)] = max(dp[(i-1, 1)], dp[(i-1, 0)])
#
#     print(max(dp[(N-1, 0)], dp[(N-1, 1)]))
#     return
#
# N = int(input())
# stairs = []
#
# for i in range(N):
#     stairs.append(int(input()))
#
# sol()

# 다른 사람 DP 풀이법

N = int(input())

step = [0]
for _ in range(N):
    tmp = int(input())
    step.append(tmp)

dp = [0] * (N + 1)

print(step)
print(dp)

if N == 1:
    print(step[1])
    exit()
dp[1] = step[1]

print(dp)

if N >= 2:
    dp[2] = step[1] + step[2]

print(dp)

for i in range(3, N+1):
    # 마지막 노드를 꼭 거쳐야 하기 때문에 step[i] 필수
    # first: 두칸 뛰고 마지막
    # second: 한칸 뛰고 마지막 + 3칸 연속 안됨 -> dp[i-2] 제외
    dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i])
    print(dp)

print(dp[N])
