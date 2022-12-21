import sys
input = sys.stdin.readline

a = int(input())
for v in range(a):
    b = list(input())
    score = 0
    sum_score = 0
    for ox in b:
        if ox == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)



