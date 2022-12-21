import sys
input = sys.stdin.readline

new_list = []
for v in range(1,11):
    a = int(input())
    b = a%42
    new_list.append(b)

print(len(set(new_list)))





