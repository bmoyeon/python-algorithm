#두 리스트 합쳐서 오름차순으로 정렬

n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
result = N + M
result.sort()
for i in result:
    print(i, end=' ')

#solution
#위의 방식대로 하면 sort()는 nlog(n)
#이미 정렬되었다는 점을 활용하여 두 리스트 원소의 합만큼 반복문 돌리면 n
n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
p1 = p2 = 0
l = []
while p1 < n and p2 < m:
    if N[p1] <= M[p2]:
        l.append(N[p1])
        p1 += 1
    else:
        l.append(M[p2])
        p2 += 1
if p1 < n:
    l = l + N[p1:]
if p2 < m:
    l = l + M[p2:]
for i in l:
    print(i, end=' ')
