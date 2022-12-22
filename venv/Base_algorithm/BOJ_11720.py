import sys
input = sys.stdin.readline

a = int(input())
b = input()

cnt = 0
for _ in range(a):
    cnt +=int(b[_])
print(cnt)