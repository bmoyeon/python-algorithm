#1부터 n까지 합 출력하기

def sum_numbers(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    print(result)

sum_numbers(10)
