from sys import stdin

def calc(numMax):
    memo = [None for _ in range(numMax + 1)]
    memo[0] = 0
    memo[1] = 1

    for x in range(2, numMax+1):
        memo[x] = memo[x-1]+memo[x-2]
    return memo

def main():
    line = int(stdin.readline())
    data = []
    
    while line != 0:
        data.append(line)
        line = int(stdin.readline())
        
    ans = calc(85)
    for x in data:
        print(ans[x])
main()
