def run():
    LIMITE = 1000000

    contador = 0
    potencia = 2**contador
    while potencia < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a ' + str(potencia))
        contador+=1
        potencia = 2**contador
    
    


if __name__ == '__main__':
    run()