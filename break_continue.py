def run():
    # for contador in range(1000):
    #     if contador % 2 == 0:
    #         continue
    #     print(contador)

    #   for contador in range(1000):
    #       if contador == 580:
    #           break
    #       print(contador)

    texto = input('Escribe Texto: ')
    for i in texto:
        if i == 'o':
            continue
        print(i)

if __name__=='__main__':
    run()