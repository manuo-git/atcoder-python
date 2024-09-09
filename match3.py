import queue

def swap_grid(grid, y, x, ny, nx):
    ngrid = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == y and j == x:
                ngrid[i][j] = grid[ny][nx]
            elif i == ny and j == nx:
                ngrid[i][j] = grid[y][x]
            else:
                ngrid[i][j] = grid[i][j]
    return ngrid

def get_clear_ij(grid):
    three = [[(0,1), (0,2)], [(1,0), (2,0)]]
    clears = set()
    for i in range(H):
        for j in range(W):
            color = grid[i][j]
            if color <= 0: continue
            ok = []
            for th in three:
                flag = True
                for t in th:
                    ni = i+t[0]
                    nj = j+t[1]
                    if not(0 <= ni < H and 0 <= nj < W):
                        flag = False
                        break
                    if grid[i+t[0]][j+t[1]] != color:
                        flag = False
                if flag: ok.append(th)
            
            for th in ok:
                clears.add((i,j))
                for t in th:
                    clears.add((i+t[0],j+t[1]))
    return clears

def clear_grid(grid, clears):
    for i, j in clears:
        grid[i][j] = -1
    return grid

def drop_grid(grid):
    for j in range(W):
        for i in range(H-1, -1, -1):
            if grid[i][j] >= 0: continue
            color = -1
            for k in range(i, -1, -1):
                if grid[k][j] == 0: break
                elif grid[k][j] > 0:
                    color = grid[k][j]
                    grid[k][j] = -1
                    break
            grid[i][j] = color
    return grid

def check_null_grid(grid):
    ret = True
    for i in range(H):
        for j in range(W):
            if grid[i][j] > 0:
                ret = False
    return ret

def get_moved(grid):
    dir = [(1,0,'D'), (0,1,'R')]
    ret = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] <= 0: continue
            for d in dir:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < H and 0 <= nj < W:
                    if grid[ni][nj] <= 0: continue
                    ngrid = swap_grid(grid, i, j, ni, nj)
                    clears = get_clear_ij(ngrid)
                    if len(clears) == 0: continue
                    while len(clears) > 0:
                        ngrid = clear_grid(ngrid, clears)
                        ngrid = drop_grid(ngrid)
                        clears = get_clear_ij(ngrid)
                    ret.append((ngrid, (i, j, d[2])))
    return ret

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(H)]

q = queue.Queue()
q.put((C,[]))

def printgrid(grid, plus = ''):
    for i in range(H):
        print(grid[i])
    print(plus)
ans = []
while q.qsize() > 0:
    grid, l = q.get()
    if check_null_grid(grid):
        for y, x, ds in l:
            ans.append((y+1, x+1, ds))
        break
    moved = get_moved(grid)
    for mg, ml in moved:
        q.put((mg, l+[ml]))

dir = {'R':(0,1), 'D':(1,0)}
grid = C.copy()
printgrid(grid)
for a in ans:
    print(a)
    i, j, _ = a
    i, j = (i-1, j-1)
    d = dir[a[2]]
    ni = i + d[0]
    nj = j + d[1]
    grid = swap_grid(grid, i, j, ni, nj)
    clears = get_clear_ij(grid)
    if len(clears) == 0: continue
    while len(clears) > 0:
        grid = clear_grid(grid, clears)
        grid = drop_grid(grid)
        clears = get_clear_ij(grid)
    printgrid(grid)

print(ans)
