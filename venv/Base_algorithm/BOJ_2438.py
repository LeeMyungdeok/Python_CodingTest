import sys
input = sys.stdin.readline
A = int(input())
for v in range(1 , A+1):
    print((" "*(A-v))+"*"*v)