#공주 구하기
#큐: 먼저 넣은 데이터가 먼저 나오는 구조로 저장하는 자료구조
#First In First Out

from collections import deque

n, k = map(int, input().split())
l = list(range(1, n+1))
l = deque(l)
while l:
    for _ in range(k-1):
        l.append(l.popleft())
    l.popleft()
    if len(l) == 1:
        print(l[0])
        break
