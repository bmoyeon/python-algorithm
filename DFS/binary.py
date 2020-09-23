#재귀함수를 이용한 이진수 출력

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end='')

n = int(input())
DFS(n)



#DFS(11) -> DFS(5) -> DFS(2) -> DFS(1) -> DFS(0) 종료!
#7번째 줄로 돌아옴
#1(DFS(1)) -> 0(DFS(2)) -> 1(DFS(5)) -> 1(DFS(11))
