def run():
    import random
    palabras = []
    with open('data.txt', "r", encoding="utf-8") as f:
        for i in f:
            i = i[:-1]
            palabras.append(i)
        
        print(random.choice(palabras))

# def run():
#     # letras_todas = []
#     # resultado = []
#     # letras = input('Digita una letra:')
    
#     print(ahorcado())
#     # for i in range(len(ahorcado())):
#     #     resultado.append("_")
    
#     #print(resultado)




if __name__=='__main__':
    run()