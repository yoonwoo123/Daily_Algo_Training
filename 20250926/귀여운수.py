import sys
sys.stdin = open("귀여운수.txt")

N = input()

for i in range(1, len(N) - 1):
    if int(N[0]) - int(N[1]) != int(N[i]) - int(N[i + 1]):
        print('흥칫뿡!! <(￣ ﹌ ￣)>')
        exit()
print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')

