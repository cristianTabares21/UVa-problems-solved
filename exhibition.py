from sys import stdin

def main():

    numCases = int(stdin.readline())
    case = 0

    while(numCases > 0):
        
        numFriends = int(stdin.readline())
        stamps = {}
        uniquesOwner = [0]*numFriends
        uniques = 0

        for x in range(numFriends):
            line = stdin.readline().split()

            for y in range(1, int(line[0])+1):
                if(line[y] in stamps.keys()):
                    stamps[line[y]].add(x)
                else:
                    stamps[line[y]] = set()
                    stamps[line[y]].add(x)
                    
        keys = stamps.keys()
        for keys in stamps:
            if(len(stamps[keys]) == 1):
                uniques += 1
                val = stamps[keys].pop()
                uniquesOwner[val] += 1

        case += 1
        print('Case {}:'.format(case), end=' ')
        if(uniques > 0):
            for k in range(len(uniquesOwner)):
                if k == len(uniquesOwner)-1:
                    print('{:.6f}%'.format(uniquesOwner[k]*100/uniques), end='')
                else:
                    print('{:.6f}% '.format(uniquesOwner[k]*100/uniques), end='')
        print()
        numCases -= 1
                
main()
