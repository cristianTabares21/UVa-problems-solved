from sys import stdin
from collections import deque

def main():
    cases = int(stdin.readline())

    while(cases > 0):
        left = deque()
        right = deque()
        line = stdin.readline()
        capFerry, timeFerry, cantCars = map(int, line.split())
        currentTime = [0]*cantCars

        for x in range(cantCars):
            line2 = stdin.readline().split()

            if(line2[1][0] == "l"):
                left.append((int(line2[0]), x))
            else:
                right.append((int(line2[0]), x))

        time, side = 0, 0
        while(len(left) != 0 or len(right) != 0):

            if(len(left) != 0 and len(right) != 0):
                time = max(time, min(left[0][0], right[0][0]))
            elif(len(left) != 0 and len(right) == 0):
                time = max(time, left[0][0])
            else:
                time = max(time, right[0][0])
                
            load = 0
            
            if(side == 0):
                while(len(left) != 0 and left[0][0] <= time and load < capFerry):
                    load += 1
                    currentTime[left[0][1]] = time + timeFerry
                    left.popleft()
                time += timeFerry
                side = 1
                
            else:
                while(len(right) != 0 and right[0][0] <= time and load < capFerry):
                    load += 1
                    currentTime[right[0][1]] = time + timeFerry
                    right.popleft()
                time += timeFerry
                side = 0

        for i in range(len(currentTime)):
            print(currentTime[i])

        if(cases-1 > 0):
            print()
        cases -= 1
main()
