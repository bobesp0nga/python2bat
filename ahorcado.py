#penasr palabra
#escribir _ _ _ _ _ _
#pedir letre
#Buscar si la letra esta en la palabra
    # Si es SÍ la letra en la palabra 
        #mirar si hemos acertado-FIN
    #Si es NO, intentos -1
        #Mirar si hemos perdido

palabrasecreta = "gato"

letrascorrectas = []
letraincorrectas = []

seguirjugando = True

while seguirjugando == True:
    for letra in palabrasecreta:
        if letra in letrascorrectas:
            print(letra, end="")
        else:
            print('_',end="")

    letrapedida = input("Dime una letra\n")
    if letrapedida in palabrasecreta:
        letrascorrectas.append(letrapedida)
    else:
        letraincorrectas.append(letrapedida)

    print(f"correctas: {letrascorrectas}")
    print(f"incorrectas: {letraincorrectas}")

    if set(letrascorrectas) == set(palabrasecreta):
        seguirjugando = False
        print("Has ganado")

    if len(letraincorrectas) == 6:
        seguirjugando == False
        print("Has perdido")