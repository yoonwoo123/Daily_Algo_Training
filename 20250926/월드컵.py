# import sys, itertools
# sys.stdin = open("월드컵.txt")
#
# ans = []
# tournaments = []
#
# for i in range(4):
#     tournaments.append(list(map(int, input().split())))
#
# for tournament in tournaments:
#     teams = []
#     for i in range(0, len(tournament), 3):
#         teams.append(tournament[i:i + 3])
#
#     possible = 1
#     breakFlag = 0
#     tot = 0
#
#     for x in range(len(teams) - 1):
#         if breakFlag == 1: break
#         for y in range(len(teams[x])):
#             if teams[x][y] > 0:
#                 for i in range(x + 1, len(teams)):
#                     if teams[i][abs(y - 2)] > 0:
#                         if teams[x][y] < 1: break
#                         teams[x][y] -= 1
#                         teams[i][abs(y - 2)] -= 1
#                 if teams[x][y] != 0:
#                     breakFlag = 1
#                     possible = 0
#                     break
#
#     for x in range(len(teams)):
#         for y in range(len(teams[x])):
#             tot += teams[x][y]
#     # print(teams)
#
#     if teams[x][y] > 0: possible = 0
#     ans.append(possible)
#
# print(' '.join(map(str, ans)))

import sys, itertools
sys.stdin = open("월드컵.txt")

ans = []
tournaments = []

for i in range(4):
    tournaments.append(list(map(int, input().split())))

for tournament in tournaments:
    teams = []
    for i in range(0, len(tournament), 3):
        teams.append(tournament[i:i + 3])

    # print(teams)
    tot = 0
    for team in teams:
        tot += sum(team)
    if tot != 30:
        ans.append(0)
        continue

    perms = list(itertools.permutations(teams, len(teams)))
    # print(perms)

    possible = 0
    for perm in perms:
        possible = 1
        for i in range(len(teams) - 1): # 6팀
            if possible == 0: break
            for j in range(3):
                if perm[i][j] > 0:
                    for k in range(i+1, len(teams)):
                        if perm[i][j] < 1: break
                        if perm[k][abs(j - 2)] > 0:
                            perm[i][j] -= 1
                            perm[k][abs(j - 2)] -= 1
                    if perm[i][j] > 0:
                        possible = 0
                        break

        tot = 0
        for i in range(len(teams)): # 6팀
            for j in range(3):
                tot += perm[i][j]

        if tot > 0: continue
        if possible == 1: break

    ans.append(possible)

print(' '.join(map(str, ans)))
