import sys
input = sys.stdin.readline
A = int(input())
t = int(input())
c = 0
for v in range(A):
    a , b = map(int, input().split(" "))
    c += a * b
if c == t:
    print("Yes")
else:
    print("No")