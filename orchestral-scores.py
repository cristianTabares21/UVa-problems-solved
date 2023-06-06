from sys import stdin
import heapq

def main():
    line = stdin.readline().split()
    while(len(line) != 0):
        cantRest = int(line[0]) - int(line[1])
        pq = []
        line2 = [int(x) for x in stdin.readline().split()]
        
        for x in range(len(line2)):
            heapq.heappush(pq, (-1*line2[x], line2[x], 2))
            
        while(cantRest > 0):
            major = heapq.heappop(pq)
            if(major[1]%(major[2]) == 0):
                div = major[1]//(major[2])
                heapq.heappush(pq, (-div, major[1], major[2]+1))
            else:
                div = (major[1]//(major[2]))+1
                heapq.heappush(pq, (-div, major[1], major[2]+1))
            cantRest -= 1
        print(pq[0][0]*-1)
        line = stdin.readline().split()
main()
