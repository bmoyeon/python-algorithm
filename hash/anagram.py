#Anagram

n = input()
m = input()
dic1 = {}
dic2 = {}

for i in n:
    dic1[i] = dic1.get(i, 0) + 1
for i in m:
    dic2[i] = dic2.get(i, 0) + 1

for i in dic1.keys():
    if i in dic2.keys():
        if dic1[i] != dic2[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')

#딕셔너리 개선코드
n = input()
m = input()
dic = {}

for i in n:
    dic[i] = dic.get(i, 0) + 1
for i in m:
    dic[i] = dic.get(i, 0) - 1

for i in n:
    if dic.get(i) > 0:
        print('NO')
        break
else:
    print('YES')
