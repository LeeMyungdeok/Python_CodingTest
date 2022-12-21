import sys
input = sys.stdin.readline

all_list = list(map(int, range(1,31)))
for v in range(1,29):
    a = int(input())
    all_list.remove(a)

print(min(all_list))
print(max(all_list))
# print(all_list)
# print(sorted(all_list , reverse= True))
# print(sorted(all_list))
# print(all_list[0])
# print(all_list[1])