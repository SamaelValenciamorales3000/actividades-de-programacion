vocales="aeiouAEIOU"
cambio="          "
result=str.maketrans(vocales,cambio)
palabra=str(input("ingresa la palabra:"))
sin_espacios=palabra.translate(result)
print(sin_espacios.replace(' ',''))
