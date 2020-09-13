#3개의 주사위를 던져서 규칙에 따라 가장 많은 상금을 받는 사람의 상금을 출력

n = int(input())

result = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    #가장 많은 상금을 받는 사람의 상금을 출력해야 하므로 제일 먼저 조건 걸어준다.
    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b or a==c:
        money = 1000 + a * 100
    #b==c를 따로 적는 이유는 money 계산시 b로 계산해야 해 서로 다르기 때문이다.
    elif b==c:
        money = 1000 + b * 100
    else:
        money = c * 100

    if money > result:
        result = money
print(result)
