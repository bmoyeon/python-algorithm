#최소힙
#힙: 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리로 구현된 자료구조
#완전이진트리: 노드를 삽입할 때 왼쪽부터 차례대로 삽입하는 트리
#최소힙: 부모 노드값이 왼쪽자식과 오른쪽자식노드의 값보다 작게 트리를 구성하는 것

import heapq as hq

l = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(l) == 0:
            print(-1)
        else:
            #root node를 pop 하고 맨 마지막 level의 오른쪽 노드를 root 로 옮겨 연산
            print(hq.heappop(l))
    else:
        hq.heappush(l, n)
