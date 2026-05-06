def find(p, i):
    return i if p[i] == i else find(p, p[i])

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    p = list(range(n))
    
    print("MST edges:")
    
    for u, v, w in edges:
        x, y = find(p, u), find(p, v)
        if x != y:
            print(u, "-", v, ":", w)
            p[x] = y

edges = [
    (0,1,10),
    (0,2,6),
    (0,3,5),
    (1,3,15),
    (2,3,4)
]

kruskal(edges, 4)