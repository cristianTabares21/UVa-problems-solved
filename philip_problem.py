from sys import stdin


def phi(n, m, T, E, memo):
    ans = None
    if (n, m) in memo:
        ans = memo[(n, m)]
    else:
        if n == len(T):
            ans = 0
        else:
            if m > 0:
                ans = min((T[n] >> 1) + phi(n+1, (m+E[n])-1, T, E,
                          memo), T[n] + phi(n+1, m+E[n], T, E, memo))
            else:
                ans = T[n] + phi(n+1, m+E[n], T, E, memo)
        memo[(n, m)] = ans
    return ans


def main():
    numTrips = int(stdin.readline())
    while (numTrips > 0):
        T, E = [], []
        for x in range(numTrips):
            line = stdin.readline()
            trip, sphe = map(int, line.split())
            T.append(trip)
            E.append(sphe)
        memo = {}
        ans = phi(0, 0, T, E, memo)
        print(ans)
        numTrips = int(stdin.readline())


main()
