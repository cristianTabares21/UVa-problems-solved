from sys import stdin


def solver(sol, solsOpt, data, currSum, obj, initIndx):
    if currSum == obj:
        if len(solsOpt) == 0 or len(sol) < len(solsOpt[0]):
            solsOpt.clear()
            solsOpt.append(list(sol))
    elif len(solsOpt) == 0 or len(sol) < len(solsOpt[0]):
        x = initIndx
        while x >= 0:
            if currSum+data[x] <= obj:
                sol.append(data[x])
                solver(sol, solsOpt, data, currSum+data[x], obj, x)
                sol.pop()
            x -= 1


def main():
    cases = int(input())
    currCase = 1
    while cases > 0:
        line = [int(x) for x in stdin.readline().split()]
        obj = line[1]
        data = [int(x) for x in stdin.readline().split()]
        solsOpt = []
        solver([], solsOpt, data, 0, obj, len(data)-1)
        print('Case {}:'.format(currCase), end='')
        if len(solsOpt) == 0:
            print(' impossible', end='')
        else:
            print(' [{}]'.format(len(solsOpt[0])), end='')
            i = 0
            while i < len(solsOpt[0]):
                print(' {}'.format(solsOpt[0][i]), end='')
                i += 1
        print()
        cases -= 1
        currCase += 1


main()
