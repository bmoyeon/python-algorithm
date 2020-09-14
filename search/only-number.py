#숫자와 문자가 섞여있는 문자열 중 숫자만 추출해 자연수를 만들고 그 약수의 개수 출력

s = input()
result = 0
for i in s:
    #isdecimal(): 문자열이 int로 변경했을 때 0-9까지의 숫자이면 True
    if i.isdecimal():
        result = result * 10 + int(i)
print(result)
count = 0
for i in range(1, result+1):
    if result % i == 0:
        count += 1
print(count)
