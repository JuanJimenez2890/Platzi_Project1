# def es_primo(numero):
#     contador = 0
#     for i in range(1,numero+1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i ==0:
#             contador+=1
#     if contador == 0:
#         return True
#     else:
#         return False


# def run():
#     numero = int(input('Escribe un numero: '))
#     if es_primo(numero):
#         print('Es primo')
#     else:
#         print('No es primo')
def validar(opcion):
    if opcion == 'Y':
        return True
    else:
        return False


def primo(num):
    
    divisibles = []
     
    for i in range(2,num+1):
        if num % i != 0:
            continue
        divisibles.append(i)
    if divisibles[0] == num:
        print('Primo')
        opcion = input('Quieres validar otro numero? Y or N: ')
        opcion = opcion[0].upper()
        
        if validar(opcion):
            return run()
        else:
            return print('bye')
    else:
        print('No primo') 
        opcion = input('Quieres validar otro numero? Y or N: ')
        opcion = opcion[0].upper()
        
        if validar(opcion):
            return run()
        else:
            return print('bye')

def run():
    num = int(input('Ingresa el numero: '))
    primo(num)

if __name__=='__main__':
    run()