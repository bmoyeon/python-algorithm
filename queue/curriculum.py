#교육과정 설계

from collections import deque

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)
    for j in plan:
        if j in dq:
            if j != dq.popleft():
                print(f'#{i+1} NO')
                break
    else:
        if len(dq) == 0:
            print(f'#{i+1} YES')
        else:
            print(f'#{i+1} NO')
