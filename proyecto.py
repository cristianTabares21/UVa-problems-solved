from sys import stdin

# Funcion que se encarga de aplicar programacion dinamica con tabulacion


def dp(cantRealms, maxLevel, damages, healts):

    # Se inicializa la matriz de tamaño N+1 * M en infinito cada posicion.
    tabu = [[float("inf") for _ in range(maxLevel+1)]
            for _ in range(cantRealms+1)]
    # La posicion N+1,M es 0 ya que para llegar al nivel N+1 no se necesitan puntos.
    tabu[cantRealms][maxLevel] = 0

    i = cantRealms-1  # Se recorre la matriz desde el ultimo reino

    if maxLevel < cantRealms:
        opt = 1  # Opcion cuando hay mas reinos que niveles por alcanzar.
    else:
        opt = 2  # Opcion cuando hay mas niveles por alcanzar que reinos.

    while i >= 0:  # Itera hasta que haya llegado al primer reino.
        if opt == 1:
            limit = 0  # Se establece un limite acorde a la opcion, cuando opt=1, quiere decir que en cada reino es posible alcanzar el nivel maximo
        elif opt == 2:
            limit = i
        ''' Mismo caso al anterior, pero cuando opt=2, el i marca cual es el nivel minimo que se tuvo que llegar al estar en un reino i,j, 
        ej: si el  ultimo reino es 3 y el nivel maximo 4, entonces el minimo nivel para llegar a ese reino es 3.'''
        j = maxLevel  # Se inicializa j siempre en el nivel maximo, para llenar tabu de derecha a izquierda.
        while j >= limit:
            # Caso base 1: Cuando esta en cualquier reino pero con el nivel maximo.
            if j == maxLevel:
                tabu[i][j] = max(1, tabu[i+1][j] - healts[j]) + damages[i][0]
            # Caso base 2: Cuando esta en cualquier reino con un nivel antes del maximo.
            elif j+1 == maxLevel:
                tabu[i][j] = max(1, tabu[i+1][j+1] -
                                 healts[j+1]) + damages[i][0]
            # Caso inductivo: Cuando en cualquier reino falta mas de un nivel para el maximo.
            elif j+1 < maxLevel:
                nrange = min(j+len(damages[i]), maxLevel)+1
                # nrange obtiene el minimo entre la cantidad de mobs en el reino y el nivel maximo para evitar probar con valores que estan fuera del rango.
                for k in range(j+1, nrange):
                    tabu[i][j] = min(
                        tabu[i][j], (max(1, tabu[i+1][k] - healts[k]) + damages[i][(k-1)-j]))
                    # Se calcula la menor vida necesaria cuando estamos en el reino i con nivel j.
            j -= 1
        i -= 1
    print(tabu)
    return tabu[0][0]  # La respuesta esta en 0,0


'''
Esta funcion es auxiliar para calcular el daño total de un grupo de mobs.
Ej: en el caso del reino 1 con mobs [2, 3, 6], esta funcion calcula la lista [2, 7, 18] que seria los respectivos daños del combate por turnos.
'''


def sumDamage(listR, listD):
    listD[0] = listR[0]
    for x in range(1, len(listR)):
        listD[x] = listD[x-1]+sum(listR[:x+1])


'''
En esta funcion main, unicamente se leen los datos, se llama a la funcion dp y se imprime el resultado.
'''


def main():
    cases = int(stdin.readline())
    while cases > 0:
        N, M = map(int, stdin.readline().split())
        healts = [int(x) for x in stdin.readline().split()]
        realms, damages = [], []
        for _ in range(N):
            line = stdin.readline().split()
            realm = [0]*(len(line)-1)
            damageRealm = [0]*(len(line)-1)
            for i in range(1, len(line)):
                realm[i-1] = int(line[i])
            realm.sort()
            sumDamage(realm, damageRealm)
            realms.append(realm)
            damages.append(damageRealm)
        ans = dp(N, M-1, damages, healts)
        print(ans)
        cases -= 1


main()
