#격자판의 각 행, 열, 대각선의 합이 가장 큰 합을 출력

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += l[i][j]
        sum2 += l[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum3 = sum4 = 0
for i in range(n):
    sum3 += l[i][i]
    sum4 += l[i][n-i-1]
if sum3 > largest:
    largest = sum3
if sum4 > largest:
    largest = sum4

print(largest)
