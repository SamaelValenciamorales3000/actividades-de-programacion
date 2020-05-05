def esprimo(numero):
    if numero<2:
        return False
        for i in range(2,numero):
            if numero%i ==0:
                return False
                return True
def serieprimo(numprimo):
    c=0
    i=0
    while c<numprimo:
        i+=1
        if esprimo(i):
            c+=1
            print(i)
serieprimo(10)
