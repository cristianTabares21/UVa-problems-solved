from sys import stdin

def binarySearch(low, hi, data, value):
    ans = None
    while low+1 != hi:
        mid = low+((hi-low)>>1)
        if data[mid] > value: hi = mid
        elif data[mid] < value: low = mid
        else: hi = mid
    ans = hi
    cantApar = data[hi]-data[hi-1]
    return ans, cantApar

def main():
    line = stdin.readline().strip()
    while(line != ""):
        data, dataOrd = [], []
        mayor = 0
        for x in range(int(line)):
            line2 = int(stdin.readline())
            if line2 > mayor:
                mayor = line2
            data.append(line2)

        dataTemp = [0]*(mayor+1)
        for j in range(len(data)):
            dataTemp[data[j]] += 1

        dataOrd.append(dataTemp[0])
        a = dataTemp[0]
        for x in range(1, len(dataTemp)):
            dataOrd.append(dataTemp[x]+a)
            a += dataTemp[x]
            
        pm = len(data)//2
        if len(data) == 1:
            print('{} {} {}'.format(data[0], 1, 1), end='')
        elif len(data)%2 == 0:
            ans = binarySearch(-1, len(dataOrd)-1, dataOrd, pm)
            ans2 = binarySearch(-1, len(dataOrd)-1, dataOrd, pm+1)
            if ans[0] == ans2[0]:
                print('{} {} {}'.format(ans[0], ans[1], (ans2[0]-ans[0])+1), end='')
            else:
                print('{} {} {}'.format(ans[0], ans[1]+ans2[1], (ans2[0]-ans[0])+1), end='')
        else:
            ans = binarySearch(-1, len(dataOrd)-1, dataOrd, pm+1)
            print('{} {} {}'.format(ans[0], ans[1], 1), end='')

        print()
        line = stdin.readline().strip()

main()
