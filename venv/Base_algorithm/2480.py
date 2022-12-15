import sys
input = sys.stdin.readline
A , B, C = map(int, input().split(" "))
if A==B==C:
    print(10000 + (A * 1000))
elif A==B:
    c1000 + (A * 100)
elif C==B:
    print(1000 + (B * 100))
elif C==A:
    print(1000 + (A * 100))
else:
    print(100 * max(A,B,C))

