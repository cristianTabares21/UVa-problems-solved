from sys import stdin
from collections import deque

def main():
    cantTeams = int(stdin.readline())
    scen=0
    
    while(cantTeams > 0):
        members = {}
        teams = []
        teamQueue = deque()
        for x in range(cantTeams):
            line = stdin.readline().split()

            for y in range(1, int(line[0])+1):
                members[line[y]] = x

            team = deque()
            teams.append(team)
            
        scen += 1
        act = stdin.readline().split()

        print('Scenario #{}'.format(scen))

        while(act[0] != "STOP"):
            if(act[0] == "ENQUEUE"):
                memTeam = members[act[1]]
                teams[memTeam].append(act[1])
                if(memTeam not in teamQueue):
                    teamQueue.append(memTeam)
                    
            elif(act[0] == "DEQUEUE"):
                head = teamQueue[0]
                if(len(teams[head]) == 1):
                    print(teams[head].popleft())
                    teamQueue.popleft()

                elif(len(teams[head]) > 1):
                    print(teams[head].popleft())
                    
            act = stdin.readline().split()

        print()
            
        cantTeams = int(stdin.readline())
            
main()
