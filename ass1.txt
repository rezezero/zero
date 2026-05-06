g = {
 'A':['B','C'],
 'B':['A','D','E'],
 'C':['A','F'],
 'D':['B'],
 'E':['B'],
 'F':['C']
}

# -------- USER INPUT VERSION (UNCOMMENT TO USE) --------
#g = {}
#n = int(input("Enter number of vertices: "))
#for _ in range(n):
     #node = input("Enter node: ")
     #neighbors = input("Enter neighbors: ").split()
     #g[node] = neighbors
# ------------------------------------------------------

def bfs(s):
    v, q = [s], [s]
    while q:
        n = q.pop(0)
        print(n, end=" ")
        for nb in g[n]:
            if nb not in v:
                v.append(nb)
                q.append(nb)

def dfs(n, v=[]):
    v.append(n)
    print(n, end=" ")
    for nb in g[n]:
        if nb not in v:
            dfs(nb, v)

#start = input("Enter starting node: ")
#bfs(start)
#dfs(start, [])

print("BFS:")
bfs('A')

print("\nDFS:")
dfs('A', [])