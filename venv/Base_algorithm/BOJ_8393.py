import sys
input = sys.stdin.readline
A = int(input())

a = 0
for v in range(A):
    a += v + 1

print(a)