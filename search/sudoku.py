#스도쿠 검사

def check(x):
    for i in range(9):
        check1 = [0]*10
        check2 = [0]*10
        for j in range(9):
            check1[x[i][j]] = 1
            check2[x[j][i]] = 1
        if sum(check1) != 9 or sum(check2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            check3 = [0]*10
            for k in range(3):
                for s in range(3):
                    check3[x[i*3+k][j*3+s]] = 1
            if sum(check3) != 9:
                return False
    return True

l = [list(map(int, input().split())) for _ in range(9)]
if check(l):
    print('YES')
else:
    print('NO')
