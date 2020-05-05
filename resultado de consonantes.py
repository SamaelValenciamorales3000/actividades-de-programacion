vocales=['a','e','i','o','u','A','E','I','O','U',' ']
palabra=str(input("ingresa la palabra:"))

for letra in palabra:
    for vocal in vocales:
     if letra == vocal:
        palabra=palabra.replace(letra,'')
print("NO.deconstante: ",len(palabra))
