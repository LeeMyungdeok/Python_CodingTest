import sys
input = sys.stdin.readline

A = int(input())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')