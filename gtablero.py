def generartablero(n,m):
    element = n*m
    tablero = []
    for e in range(n):
        subt=[]
        for i in range(m):
            if e % 2 == 0:
                subt.append(element)
                
            else:
                subt.insert(0,element)
            element-=1
        tablero.append(subt)
    return tablero
