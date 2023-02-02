import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    c = deque(map(int,sys.stdin.readline().split()))

