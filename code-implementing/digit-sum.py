#입력된 자연수 중 자릿수의 합이 가장 큰 자연수 구하기

n = int(input())
l = list(map(int, input().split()))

def digit_sum(x):
    result = 0
    #또 다른 방법: 10으로 나눈 나머지와 몫을 이용
    #result += x%10
    #x = x//10
    for i in str(x):
        result += int(i)
    return result

max_total = -2147000000
for x in l:
    total = digit_sum(x)
    if total > max_total:
        max_total = total
        result = x
print(x)
