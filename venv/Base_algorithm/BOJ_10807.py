import sys
input = sys.stdin.readline
a = int(input())
a_list = list(map(int, input().split()))
v = int(input())
print(a_list.count(v))