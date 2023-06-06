from sys import stdin


def main():
    cases = int(stdin.readline())

    while cases > 0:

        data = [int(x) for x in stdin.readline().split()]
        dataAux = {}
        pairs = (data[0]*2)+1

        for x in range(1, pairs):
            dataAux[data[x]] = []

        for x in range(1, pairs):
            dataAux[data[x]].append(x)

        swaps = 0
        i = 1
        while i < pairs:
            if data[i] != data[i+1]:
                temp = data[i+1]
                tempAux = dataAux[data[i]][1]
                tempAux2 = dataAux[data[i+1]][1]
                data[tempAux] = temp
                dataAux[temp][0] = min(tempAux, tempAux2)
                dataAux[temp][1] = max(tempAux, tempAux2)
                swaps += 1
            i += 2
        print(swaps)
        cases -= 1


main()
