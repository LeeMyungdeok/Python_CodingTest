import sys
input = sys.stdin.readline
a = 0
len_list = []
for v in range(1,10):
    b = int(input())
    len_list.append(b)
    if v == 1:
        a = b
        # print(a)
    elif a > b:
        pass
        # print(a)
    elif b > a:
        a = b
        # print(a)
print(a)
print(len_list.index(a)+1)

