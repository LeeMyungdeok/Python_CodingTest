import sys
input = sys.stdin.readline
A = int(input())

for i in range(A):
    A,B = map(int,input().split())
    print(A+B)
