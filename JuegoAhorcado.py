def run():
    import random
    import os
    palabras = []
    with open('data.txt', "r", encoding="utf-8") as f:
        for i in f:
            i = i[:-1]
            palabras.append(i)
        
        palabra = random.choice(palabras)
        
        resultado = []
        letras_todas = []
        intentos = len(palabra)
        fallos = 0
        correcta = []
        

        while intentos > 0:
            
            for i in palabra:
                if i in letras_todas:
                    print(i,end="")
                    
                    
                else:
                    print("_", end="")
                    fallos += 1
            if fallos == 0:    
                print("Ganaste")
                break
        
            letra = input("Introduce una letra:")
            letras_todas += letra
            
            if letra not in palabra:
                intentos -=1
                print(f'Restan {intentos} intentos')
        else:
            print('Gracias por participar')
            print(f'{palabra} era la palabra')
        

        
      

            




    # for i in range(len(ahorcado())):
    #      resultado.append("_")
    
    # print(resultado)




if __name__=='__main__':
    run()