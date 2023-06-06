from sys import stdin
from heapq import heappop, heappush


def Dijkstra(A, B, C, D):
    pq = [(0, (0, 0, C))]
    visited = set()
    salida = 1
    minObt = -float('inf')
    costObt = 0
    while len(pq) != 0 and salida == 1:
        cost, u = heappop(pq)

        if u[0] == D or u[1] == D or u[2] == D:
            ans = (cost, D)
            salida = 0

        else:
            if u not in visited:
                visited.add(u)
                countA, countB, countC = u[0], u[1], u[2]

                if minObt < countA and countA < D:
                    minObt = countA
                    costObt = cost
                if minObt < countB and countB < D:
                    minObt = countB
                    costObt = cost
                if minObt < countC and countC < D:
                    minObt = countC
                    costObt = cost

                ans = (costObt, minObt)

                if countA > 0:
                    wtrmv = min(countA, B-countB)
                    newNode = (countA-wtrmv, countB+wtrmv, countC)
                    if newNode not in visited:
                        heappush(pq, (cost+wtrmv, newNode))

                    wtrmv = min(countA, C-countC)
                    newNode2 = (countA-wtrmv, countB, countC+wtrmv)
                    if newNode2 not in visited:
                        heappush(pq, (cost+wtrmv, newNode2))

                if countB > 0:
                    wtrmv = min(countB, A-countA)
                    newNode = (countA+wtrmv, countB-wtrmv, countC)
                    if newNode not in visited:
                        heappush(pq, (cost+wtrmv, newNode))

                    wtrmv = min(countB, C-countC)
                    newNode2 = (countA, countB-wtrmv, countC+wtrmv)
                    if newNode2 not in visited:
                        heappush(pq, (cost+wtrmv, newNode2))

                if countC > 0:
                    wtrmv = min(countC, A-countA)
                    newNode = (countA+wtrmv, countB, countC-wtrmv)
                    if newNode not in visited:
                        heappush(pq, (cost+wtrmv, newNode))

                    wtrmv = min(countC, B-countB)
                    newNode2 = (countA, countB+wtrmv, countC-wtrmv)
                    if newNode2 not in visited:
                        heappush(pq, (cost+wtrmv, newNode2))
    return ans


def main():
    cases = int(stdin.readline())
    while cases > 0:
        data = [int(x) for x in stdin.readline().split()]
        A, B, C, D = data[0], data[1], data[2], data[3]
        if max(A, B, C, D) == D or D > C:
            print('{} {}'.format(0, C))
        else:
            wMove, minObt = Dijkstra(A, B, C, D)
            print('{} {}'.format(wMove, minObt))

        cases -= 1


main()
