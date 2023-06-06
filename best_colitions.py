from sys import stdin


def phi(n, x, data, memo):
    ans = None
    N = len(data)
    if (n, x) in memo:
        ans = float(memo[(n, x)])
    else:
        if x > 50:
            ans = float(data[0]/x)

        elif n == N:
            ans = 0

        elif n != N:
            ans = max(phi(n+1, x, data, memo),
                      phi(n+1, x+data[n], data, memo))

        memo[(n, x)] = float(ans)
    return ans


def main():
    n, x = map(int, stdin.readline().split())
    while (n != 0 and x != 0):

        data = []
        memo = {}
        ans = None
        for i in range(n):
            line = float(stdin.readline())
            data.append(line)

        data[0], data[x-1] = data[x-1], data[0]

        ans = float(phi(1, data[0], data, memo))
        print('{:.2f}'.format(ans*100))
        n, x = map(int, stdin.readline().split())


main()
