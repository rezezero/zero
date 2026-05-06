g = [
    [0,2,0,6,0],
    [2,0,3,8,5],
    [0,3,0,0,7],
    [6,8,0,0,9],
    [0,5,7,9,0]
]

n = 5

def prim():
    sel = [False]*n
    sel[0] = True
    
    print("Edges in MST:")
    
    for _ in range(n-1):
        x, y, mn = 0, 0, 999999
        
        for i in range(n):
            if sel[i]:
                for j in range(n):
                    if not sel[j] and g[i][j] and g[i][j] < mn:
                        mn = g[i][j]
                        x, y = i, j
        
        print(x, "-", y, ":", g[x][y])
        sel[y] = True

prim()