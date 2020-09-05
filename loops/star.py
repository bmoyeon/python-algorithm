#별문자를 오름차순으로 출력하기
def asc_star():
    for i in range(5):
        for j in range(i+1):
            print('*', end=' ')
        print()

#별문자를 내림차순으로 출력하기
def desc_star():
    for i in range(5):
        for j in range(5-i):
            print('*', end=' ')
        print()

asc_star()
desc_star()
