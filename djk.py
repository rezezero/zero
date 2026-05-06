g = [
    [0,10,0,0,5],
    [10,0,1,0,2],
    [0,1,0,4,0],
    [0,0,4,0,3],
    [5,2,0,3,0]
]

n = 5

def dijkstra(src=0):
    dist = [999999]*n
    vis = [False]*n
    dist[src] = 0

    for _ in range(n):
        u = min((i for i in range(n) if not vis[i]), key=lambda i: dist[i])
        vis[u] = True

        for v in range(n):
            if g[u][v] and not vis[v] and dist[u] + g[u][v] < dist[v]:
                dist[v] = dist[u] + g[u][v]

    print("Distances from source:")
    print(dist)

dijkstra()