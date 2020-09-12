#k번째 수 구하기

def k_number(n, s, e, k, *args):
    l = list(args)
    new_l = l[s-1:e]
    new_l.sort()
    return new_l[k-1]

#soulution
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = l[s-1:e]
    l.sort()
    print(f'#{t+1} {l[k-1]}')
