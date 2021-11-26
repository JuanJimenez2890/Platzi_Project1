def run():
    # nombre = input('Escribre tu nombre: ')
    # for i in nombre:
    #     print(i)

    frase = input('Escribe una frase: ')
    frase = frase.replace(' ','')
    for i in frase:
        print(i.upper())


if __name__=='__main__':
    run()