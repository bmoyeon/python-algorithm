#평균점수와 가장 가까운 점수 구하기

n = int(input())
l = list(map(int, input().split()))

avg = sum(l) / len(l)
avg += 0.5
#int(67.7) = 67
avg = int(avg)
#정수형 최댓값: 2,147,483,647
min = 2147000000
for i, x in enumerate(l):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        result = i + 1
    elif tmp == min:
        if x > score:
            score = x
            result = i + 1
print(avg, result)
