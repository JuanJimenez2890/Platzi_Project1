import random

def run():
    aleatorio = random.randint(1,100)
    numero = int(input('Ingresa el numero: '))
    while numero != aleatorio:
        if numero<aleatorio:
            print('Digita un numero mas grande: ')
            numero = int(input('Elige otro numero: '))
        else:
            print('Busca un numero mas pequeño')
        numero = int(input('Elige otro numero: '))

    print('Ganaste')






if __name__=='__main__':
    run()