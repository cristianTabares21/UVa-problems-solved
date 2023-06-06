from sys import stdin

def calcThief(cordT, velT):
    newX = cordT[0] + velT[0]
    newY = cordT[1] + velT[1]
    cordT[0], cordT[1] = newX, newY

def calcCop(cordC, velC):
    newX = cordC[0] + velC[0] + 1
    newY = cordC[1] + velC[1] + 1 
    newU = newX - cordC[0]
    newV = newY - cordC[1]
    cordC[0], cordC[1] = newX, newY
    velC[0], velC[1] = newU, newV

def main():
    data = stdin.readline().split()
    while len(data) != 0:
        cordT, velT = [int(data[0]), 0], [int(data[1]), int(data[2])]
        cordC, velC = [0, 0], [0, 0]

        k = 0
        while cordC[0] < cordT[0] or cordC[1] < cordT[1]:
            k += 1
            calcThief(cordT, velT)
            calcCop(cordC, velC)
        print(k)
        data = stdin.readline().split()
main()