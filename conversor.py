def conversor(tipo_pesos, valor_dolar):
    
    pesos = int(input('Cuantos pesos' + tipo_pesos + "tienes: "))
    pesos = float(pesos)
    dolares = round(pesos/valor_dolar,2)
    dolares = str(dolares)
    print('Tienes '+dolares+' dolares')


menu = '''Conversor de monedas ✌

1-COP
2-ARS
3-MXN
2
Elige una opciòn
'''
# def suma(a,b):
#     print('La suma es:')
#     resultado = a +b
#     return resultado

# sumatoria = suma(2,4)
# print(sumatoria)

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print('Ingresa opcion correcta')

