from sys import stdin


def isValid(mid, data, numBoxes):
    ans = None
    cont = 0
    i = 0
    while i < len(data):
        if data[i] <= mid:
            cont += 1
        else:
            tmp = data[i]
            while tmp > 0:
                tmp -= mid
                cont += 1
        i += 1

    if cont <= numBoxes:
        ans = True
    else:
        ans = False

    return ans


def binarySearch(low, hi, data, numBoxes):
    while (low+1 != hi):
        mid = low+((hi-low) >> 1)

        if isValid(mid, data, numBoxes):
            hi = mid
        else:
            low = mid

    return hi


def main():
    numCities, numBoxes = map(int, stdin.readline().split())

    while (numCities != -1 and numBoxes != -1):
        data = []
        for i in range(numCities):
            line = int(stdin.readline())
            data.append(line)

        ignore = stdin.readline()

        low, hi = 0, sum(data)
        ans = binarySearch(low, hi, data, numBoxes)
        print(ans)
        numCities, numBoxes = map(int, stdin.readline().split())


main()
