g=[[0,1,1,1],
   [1,0,1,0],
   [1,1,0,1],
   [1,0,1,0]
   ]
m=3

def safe(color,node,c):
    return all(g[node][i]!=1 or color[i]!=c for i in range(len(g)))

def solve(color,node=0):
    if node==len(g):print("Coloring:",color);return
    for c in range(1,m+1):
        if safe(color,node,c):
            color[node]=c
            solve(color,node+1)
            color[node]=0

solve([0]*len(g))
