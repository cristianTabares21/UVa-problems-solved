from sys import stdin
from collections import deque


def main():
    cases = int(stdin.readline())

    while cases > 0:
        times = deque()
        cap, ferryTime, cantCars = map(int, stdin.readline().split())
        for _ in range(cantCars):
            timeCar = int(stdin.readline())
            times.append(timeCar)

        comp = cantCars % cap
        trips = 0
        last = 0
        totalTime = 0
        minTime = 0

        if comp > 0:
            for _ in range(comp):
                minTime = times.popleft() + ferryTime*2
            trips += 1

        while len(times) != 0:
            load = 0
            while load < cap and len(times) != 0:
                last = times.popleft()
                if minTime > last:
                    totalTime = minTime
                else:
                    totalTime = last
                load += 1

            minTime = totalTime + ferryTime*2
            trips += 1

        print('{} {}'.format(minTime-ferryTime, trips))
        cases -= 1


main()
