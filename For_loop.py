def validar(decision):
    if decision == 'Y':
        return True
    else:
        return False

def run():
    menu = ('Tablas del 1 al 10, digita el numero de tu elección:')
    numero = int(input(menu))
    
    for i in range(11):
        print(i*numero)

    decision = input('Quieres validar otra opción? Digita Y or N para continuar: ')
    decision = decision.upper()

    if validar(decision) == True:
        return run()
    else:
        return print('Adios')



if __name__=='__main__':
    run()