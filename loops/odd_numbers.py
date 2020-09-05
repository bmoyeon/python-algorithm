#1부터 n까지 홀수 출력하기

def odd_numbers(n):
    for i in range(1, n+1):
        if i % 2  == 1:
            print(i)

odd_numbers(50)
