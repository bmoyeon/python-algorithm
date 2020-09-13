#두 정다면체 수의 합 중 가장 확률이 높은 숫자

n, m = map(int, input().split())
l = [0]*(n+m+1)
max_score = -2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        l[i+j] += 1

for i in range(n+m+1):
    if l[i] > max_score:
        max_score = l[i]
for i in range(n+m+1):
    if l[i] == max_score:
        print(i, end=' ')
