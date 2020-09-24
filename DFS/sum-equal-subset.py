#합이 같은 부분집합

#L: 인덱스 번호
#s: 합
def DFS(L, s):
    if s > total // 2:
        return
    if L == n:
        if s == (total - s):
            print('YES')
            return
    else:
        DFS(L + 1, s + l[L])
        DFS(L + 1, s)

n = int(input())
l = list(map(int, input().split()))
total = sum(l)

DFS(0, 0)
