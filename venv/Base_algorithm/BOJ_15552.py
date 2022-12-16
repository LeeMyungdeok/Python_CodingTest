import sys
input = sys.stdin.readline
A = int(input())
for v in range(A):
    a,b = map(int, input().split(" "))
    sum = a+b
    print(sum)

