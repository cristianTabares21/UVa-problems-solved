from sys import stdin


def solver(dif, data, i, j, currDif, sol):
    if i >= j:
        if len(sol) == 0 or currDif < sol[0]:
            sol.clear()
            sol.append(currDif)

    elif i < j and currDif <= dif:
        if data[i] == data[j]:
            solver(dif, data, i+1, j-1, currDif, sol)
        elif data[i] != data[j] and currDif < dif:
            solver(dif, data, i+1, j, currDif+1, sol)
            solver(dif, data, i, j-1, currDif+1, sol)


def main():
    cases = int(stdin.readline())
    numCase = 1
    while cases > 0:
        line = stdin.readline()
        cNums, dif = map(int, line.split())
        data = [int(x) for x in stdin.readline().split()]
        sol = []
        solver(dif, data, 0, cNums-1, 0, sol)
        if len(sol) == 0:
            ans = -1
        else:
            ans = sol[0]

        print('Case {}:'.format(numCase), end='')
        if ans == 0:
            print(' Too easy', end='')
        elif ans != -1 and ans <= dif:
            print(' {}'.format(ans), end='')
        elif ans == -1:
            print(' Too difficult', end='')
        print()
        cases -= 1
        numCase += 1


main()
