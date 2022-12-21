import sys
input = sys.stdin.readline
a, b = map(int, input().split(" "))
a_list = list(map(int, input().split(" ")))

new_list = []
for v in a_list:
    if v < b:
        print(v, end=" ")


# print(A[i], end=" ")
