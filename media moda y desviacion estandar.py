import statistics
lista=[]
cantidad=int(input("¿cuantos numeros ingresaras?\nrepuestas"))

for x in range(1,cantidad+1):
    num=int(input(f"numero {x}:"))
    lista.append(num)
lista.sort()
print("ingresa los numeros",lista)
print("media",round(statistics.mean(lista),2))
print("moda",statistics.mode(lista))
print("desviacion estandar:",round(statistics.stdev(lista),2))
