#n의 약수 출력하기

def factor(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

factor(16)
