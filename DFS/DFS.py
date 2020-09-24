#이진트리 순회 (깊이우선탐색)
#전위순회: root(부모노드) -> left(왼쪽자식노드) -> right(오른쪽자식노드)
#중위순회: left(왼쪽자식노드) -> root(부모노드) -> right(오른쪽자식노드)
#후위순회: left(왼쪽자식노드) -> right(오른쪽자식노드) -> root(부모노드)

#전위순회
def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        #left
        DFS(v*2)
        #right
        DFS(v * 2 + 1)

DFS(1)
#DFS(1)-13 -> DFS(2)-13 -> DFS(4)-13 -> DFS(8) 종료 -> DFS(4)-15 -> DFS(9) 종료 ->
#DFS(2)-15 -> DFS(5)-13 -> DFS(10) 종료 -> DFS(5)-15 -> DFS(11) 종료 ->
#DFS(1)-15 -> DFS(3)-13 -> DFS(6)-13 -> DFS(12) 종료 -> DFS(6)-15 -> DFS(13) 종료 ->
#DFS(3)-15 -> DFS(7)-13 -> DFS(14) 종료 -> DFS(7)-15 -> DFS(15) 종료

#중위순회
def DFS(v):
    if v > 7:
        return
    else:
        #left
        DFS(v*2)
        print(v, end=' ')
        #right
        DFS(v * 2 + 1)

DFS(1)

#후위순회
def DFS(v):
    if v > 7:
        return
    else:
        #left
        DFS(v*2)
        #right
        DFS(v * 2 + 1)
        print(v, end=' ')

DFS(1)
