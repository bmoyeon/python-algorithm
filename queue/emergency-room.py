#응급실

from collections import deque

n, m = map(int, input().split())
l = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
l = deque(l)

count = 0
while True:
    cur = l.popleft()
    if any(cur[1] < i[1] for i in l):
        l.append(cur)
    else:
        count += 1
        if cur[0] == m:
            print(count)
            break
