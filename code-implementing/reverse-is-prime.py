#자연수 n을 뒤집은 값이 소수이면 n 출력

n = int(input())
l = list(map(int, input().split()))

def reverse(x):
    num = 0
    while x > 0:
        t = x % 10
        num = num * 10 + t
        x = x // 10
    return num

def isPrime(x):
    if x == 1:
        return False
    #약수가 존재하면 소수가 아님
    #약수는 1과 자기자신을 제외한 2로 나눈 몫을 최대로 가진다.
    #16을 예로 들면 1과 16을 제외하고, 2*8로 8이 약수들 중 최댓값이 된다.
    #나머지가 0이면 약수라는 뜻이므로 소수가 아니다.
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

for x in l:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
