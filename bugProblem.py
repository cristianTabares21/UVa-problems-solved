from sys import stdin   
import math

# Creditos al profesor Carlos Ramirez, por hacer uso de sus implementaciones para el algoritmo de Kruskal :) ....

def makeSet(v, p, rang):
    p[v], rang[v] = v, 0

def findSet(v, p):
    ans = None
    if v == p[v]: ans = v
    else: 
        p[v] = findSet(p[v], p)
        ans = p[v]
    return ans

def unionSet(u, v, p, rang):
    u,v = findSet(u, p), findSet(v, p)
    if u != v: 
        if rang[u] < rang[v]: u, v = v, u
        p[v] = u
        if rang[u] == rang[v]: rang[u] += 1

def MST(arist, numTR, numNodes, p, rang):
    mst = []

    for i in range(numNodes):
        makeSet(i, p, rang)
    arist.sort()
    cont = 0
    i = 0
    while i < len(arist) and cont <= (numNodes-1)-numTR:
        u = arist[i][1]
        v = arist[i][2]

        if findSet(u, p) != findSet(v, p):
            mst.append(arist[i])
            cont += 1 
            unionSet(u, v, p, rang)
        i += 1
    return mst

def main():
    cases = int(stdin.readline())
    while cases > 0:
        numTR = int(stdin.readline())
        nodes, arist = [], []
        node = stdin.readline().split()
        while (node[0] != '-1'):
            nodes.append((int(node[0]), int(node[1])))
            node = stdin.readline().split()

        for i in range(len(nodes)-1):
            for j in range(i+1, len(nodes)):
                dist = math.sqrt((nodes[j][0]-nodes[i][0])**2 + (nodes[j][1]-nodes[i][1])**2)
                arist.append((dist, i, j))
        
        p = [0]*len(nodes) 
        rang = [0]*len(nodes)

        ans = MST(arist, numTR, len(nodes), p, rang)
        print(math.ceil(ans[-1][0]))

        cases -= 1
main()