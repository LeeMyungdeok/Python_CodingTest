import sys
input = sys.stdin.readline
a = int(input())
num = a
cnt = 0

while True:
    b = num//10  # 2
    c = num%10   # 6
    d = (b+c)%10 # 8
    num = (c*10) + d
    cnt += 1
    if num ==a:
        break
print(cnt)