graph={
 'A':{'B':1,'C':3},
 'B':{'D':3,'E':1},
 'C':{'F':5},
 'D':{},
 'E':{'G':2},
 'F':{},
 'G':{}
}

h={
 'A':7,'B':6,'C':2,
 'D':6,'E':1,'F':6,'G':0  #estimate distance from a,b,c,d... to goal
}

def a_star(s, goal):
    open=[s]
    g={s:0}
    p={s:None}

    while open:
        c=min(open, key=lambda n:g[n]+h[n])

        if c==goal:
            path=[]
            while c:
                path.append(c)
                c=p[c]
            print(path[::-1])
            return

        open.remove(c)

        for n,cost in graph[c].items():
            tg=g[c]+cost
            if tg<g.get(n,float('inf')):
                g[n]=tg
                p[n]=c
                open.append(n)

a_star('A','G')