import sys
input = sys.stdin.readline
i = 1
while i < 6:
    a, b = map(int, input().split(" "))
    i += 1
    if i == 6:
        break
    print(a + b)