import sys
input = sys.stdin.readline
x , y = map(int, input().split(" "))

if y >= 45:
    print(x, (y-45))
else:
    if x == 0 :
        print((x+24-1) ,(y+60-45))
    else:
        print((x - 1), (y + 60 - 45))



