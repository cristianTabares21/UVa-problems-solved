from sys import stdin


def main():
    lRoad, cantStations = map(int, stdin.readline().split())
    while lRoad != 0 and cantStations != 0:
        x = 0
        data = []
        while x < cantStations:
            posX, rad = map(int, stdin.readline().split())
            data.append([posX-rad, posX+rad])
            x += 1

        data.sort()
        ans, x, ran, tmp = 0, 0, 0, 0
        flag = False
        while ran < lRoad and not flag:
            valid = False
            while x < len(data) and data[x][0] <= ran:
                valid = True
                tmp = max(tmp, data[x][1])
                x += 1

            if not valid:
                flag = True
            ran = tmp
            ans += 1

        if ran < lRoad:
            print("-1")
        else:
            print(cantStations-ans)

        lRoad, cantStations = map(int, stdin.readline().split())


main()
