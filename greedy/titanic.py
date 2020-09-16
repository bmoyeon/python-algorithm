#침몰하는 타이타닉

n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()

count = 0
while w:
    if len(w) == 1:
        count += 1
        break
    if w[0] + w[-1] > m:
        w.pop()
        count += 1
    else:
        w.pop(0)
        w.pop()
        count += 1
print(count)

#리스트는 pop(0)을 하게되면 요소를 한 칸씩 당기기 때문에 비효율적이다.
#deque는 양방향에서 데이터를 처리할 수 있는 자료구조이다.
from collections import deque
n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
w = deque(p)

count = 0
while w:
    if len(w) == 1:
        count += 1
        break
    if w[0] + w[-1] > m:
        w.pop()
        count += 1
    else:
        #popleft(): 리스트에서 pop(0)과 같은 의미
        w.popleft()
        w.pop()
        count += 1
print(count)

