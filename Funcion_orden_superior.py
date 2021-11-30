from functools import reduce

lista = [2,4,5,6,8,21,144,29,79,2,15454]
lista2 = [2,2,2]

pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)

cuadrado = list(map(lambda x:  x**2, lista))
print(cuadrado)

multiplicar_lista = reduce(lambda a,b: a *b, lista2 )
print(multiplicar_lista)