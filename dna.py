from sys import stdin


def solver(cad, cantMut, sols, currCad, dif, DNA):
    if len(currCad) == len(cad) and dif <= cantMut:
        sols.append(currCad)

    elif len(currCad) < len(cad) and dif <= cantMut:
        currIdx = len(currCad)
        for x in DNA:
            if x != cad[currIdx]:
                solver(cad, cantMut, sols, currCad + x, dif + 1, DNA)
            else:
                solver(cad, cantMut, sols, currCad + x, dif, DNA)


def main():
    cases = int(stdin.readline())
    while cases > 0:
        lenCad, cantMut = map(int, stdin.readline().split())
        cad = stdin.readline().strip()

        if cantMut == 0:
            print("1")
            print(cad)
        else:
            sols = []
            currCad = ""
            DNA = ["A", "C", "G", "T"]
            solver(cad, cantMut, sols, currCad, 0, DNA)
            print(len(sols))
            for x in sols:
                print(x)
        cases -= 1


main()
