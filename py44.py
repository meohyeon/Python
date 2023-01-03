from collections import deque
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
q = deque()
q.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [[0 for _ in range(100)] for _ in range(100)]
arr[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        bx = x + dx[i]
        by = y + dy[i]
        if bx < 0 or bx >= len(maps) or by < 0 or by >= len(maps[0]):
            continue
        if maps[bx][by] == 0 or arr[bx][by]!=0:
            continue
        arr[bx][by] = arr[x][y] +1 
        q.append((bx,by))
if arr[len(maps)-1][len(maps[0])-1] == 0:
    arr[len(maps)-1][len(maps[0])-1] = -1
print(arr[len(maps)-1][len(maps[0])-1])