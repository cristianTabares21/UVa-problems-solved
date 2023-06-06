from sys import stdin


def isSort(data):
    ans = True
    x = 0
    while x < len(data)-1 and ans:
        if data[x] > data[x+1]:
            ans = False
        x += 1
    return ans


def solver(data, sol, sols, start, end):
    if start == end:
        if len(sols) == 0 or len(sol) < len(sols[0]):
            sols.clear()
            sols.append(list(sol))
        elif len(sols) == 0 or len(sol) == len(sols[0]):
            sols.append(list(sol))

    else:
        if len(sols) == 0 or len(sol) < len(sols[0]):
            for i in range(0, len(data)-1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
                    sol.append(data[i])
                    solver(data, sol, sols, start+1)
                    data[i], data[i+1] = data[i+1], data[i]
                    sol.pop()


def main():
    line = stdin.readline().split()
    case = 1
    while line[0] != '0':
        data = []
        for x in range(1, len(line)):
            data.append(int(line[x]))

        sols = []
        solver(data, [], sols, False)
        print('There are {} swap maps for input data set {}.'.format(
            len(sols), case))
        case += 1
        line = stdin.readline().split()


main()
