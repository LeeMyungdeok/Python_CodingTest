import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split(" ")))

new_list = []
for v in range(a):
    c = b[v]/max(b)*100
    new_list.append(c)

print(sum(new_list) / len(new_list))