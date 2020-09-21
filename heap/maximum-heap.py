#최대힙

import heapq as hq
#heapq는 최소힙을 기본으로 한다. 때문에 최대합으로 사용하려면 '-'를 붙여 사용한다.

l = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(l) == 0:
            print(-1)
        else:
            print(-hq.heappop(l))
    else:
        hq.heappush(l, -n)
