from sys import stdin

def phi(n, x, data, dists, memo, T1, T2):
    ans = None
    N = len(data)
    if (n, x) in memo: ans = memo[(n, x)]
    else:
        if n == N-1 and x == -1: ans = T1
        elif n == N-1 and x != -1: ans = 0
        elif n != N-1 and x != -1:
            ans = phi(n+1, max(x-dists[n], -1), data, dists, memo, T1, T2)
        else:
            ans = min(T1 + phi(n+1, max(T1-dists[n], -1), data, dists, memo, T1, T2) ,
                      T2 + phi(n+1, max(T2-dists[n], -1), data, dists, memo, T1, T2))

        memo[(n, x)] = ans
    return ans


def main():

    line = stdin.readline().split()
    while len(line)!=0:
        numHoles = int(line[0])
        circ = int(line[1])
        T1 = int(line[2])
        T2 = int(line[3])
        if T1 > T2: T1, T2 = T2, T1
        memo = {}

        data = [int(x) for x in stdin.readline().split()]
        dists = []
        calcs = []
        for x in range(len(data)-1):
            dists.append(data[x+1]-data[x])

        ans = phi(0, -1, data, dists, memo, T1, T2)
        calcs.append(ans)
        
        
        pos = -1
        shift = 0
        lastItem = data[-1]
        firstItem = data[0]
        
        while firstItem+(circ-lastItem)<=T2 and shift+1 != len(data):
            pos -= 1
            lastItem = data[pos]
            shift += 1
        copyData = data
        while shift != 0:
            diff = circ-copyData[-1]
            copyData.pop()
            dists.clear()
            memo.clear()
            for x in range(len(copyData)): copyData[x] += diff
            copyData.insert(0,0)
            for x in range(len(copyData)-1): dists.append(copyData[x+1]-copyData[x])
            ans = phi(0, -1, copyData, dists, memo, T1, T2)
            calcs.append(ans)
            shift -= 1
        print(min(calcs))
        
        line = stdin.readline().split()
    
main()
