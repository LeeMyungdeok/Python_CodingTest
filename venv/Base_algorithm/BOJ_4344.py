import sys
input = sys.stdin.readline

test_case = int(input())
for v in range(test_case):
    std_list = list(map(int, input().split(" ")))
    nuew = std_list.copy()
    del std_list[0]
    # 다음에는 이렇게 하지말고 sum(std_list[1:])/nums[0] 해서 평균 구해라라
   tot = sum(std_list) / nuew[0]
    win_list = []
    for st in std_list:
        if st > tot:
            win_list.append(st)
    n = len(win_list)/len(std_list)*100
    print(f"{n:.3f}%")

