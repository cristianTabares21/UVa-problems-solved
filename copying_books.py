from sys import stdin

def isValid(pages, cap, scrbs):
    ans = None
    i, j = 0, 0
    while(i < scrbs):
        acum = 0
        while(j < len(pages) and acum+pages[j] <= cap):
            acum += pages[j]
            j += 1
        i += 1

    if(j < len(pages)): ans = False
    else: ans = True
    return ans

def binarySearch(low, hi, pages, scrbs):
    ans = 0
    while(low+1 != hi):
        mid = low+((hi-low)>>1)
        if(isValid(pages, mid, scrbs)): hi = mid
        else: low = mid

        if(low == hi): ans = low
        if(isValid(pages, low, scrbs)): ans = low
        else: ans = hi
        #print(ans)
    return ans

def main():
    cases = int(stdin.readline())
    
    while cases > 0:
        line = stdin.readline()
        cantPgs, scrbs = map(int, line.split())
        pages = [int(x) for x in stdin.readline().split()]
        capMax = 0

        #OUTPUT 1:
        if(scrbs == 1):
            for x in range(len(pages)):
                if(x == len(pages)-1): print('{}'.format(pages[x]), end='')
                else: print('{} '.format(pages[x]), end='')

        #OUTPUT 2:
        elif(cantPgs - scrbs == 0):
            for x in range(len(pages)):
                if(x == len(pages)-1): print('{}'.format(pages[x]), end='')
                else: print('{} / '.format(pages[x]), end='')
                
        else:
            mat = []
            capMax = binarySearch(0, sum(pages), pages, scrbs)
            i, j, ind = 0, scrbs, cantPgs
            k = cantPgs-1
            while(i < scrbs):
                lis = []
                ac = 0
                while(k >= 0 and ac + pages[k] <= capMax and ind >= j):
                    lis.append(pages[k])
                    ac += pages[k]
                    k -= 1
                    ind -= 1
                mat.append(lis)
                j -= 1
                i += 1

            #OUTPUT 3:
            x = len(mat)-1
            while(x >= 0):
                y = mat.pop()
                i = len(y)-1
                if(x > 0):
                    while(i >= 0):
                        if(i == 0): print('{}'.format(y[i]), end='')
                        else: print('{} '.format(y[i]), end='')
                        i-=1
                    print(' / ', end='')
                else:
                    while(i >= 0):
                        if(i == 0): print('{}'.format(y[i]), end='')
                        else: print('{} '.format(y[i]), end='')
                        i-=1
                x-=1
        print()
        cases -= 1
main()
